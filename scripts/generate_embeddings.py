"""
Generate Embeddings and Load to Qdrant
Physical AI Textbook RAG System - Phase 3 Task 3.2

This script:
1. Loads textbook chunks from chunks-map.json
2. Generates OpenAI embeddings for each chunk
3. Uploads chunks with embeddings to Qdrant Cloud
4. Stores chunk metadata in Neon Postgres database
"""

import json
import os
import sys
from typing import List, Dict
from dotenv import load_dotenv
import openai
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import psycopg2
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_URL = os.getenv("QDRANT_CLUSTER_URL")
NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "1536"))

# Validate configuration
if not all([OPENAI_API_KEY, QDRANT_API_KEY, QDRANT_CLUSTER_URL, NEON_DATABASE_URL]):
    print("Error: Missing required environment variables. Check your .env file.")
    sys.exit(1)

# Initialize clients
openai.api_key = OPENAI_API_KEY
qdrant_client = QdrantClient(url=QDRANT_CLUSTER_URL, api_key=QDRANT_API_KEY)

def load_chunks() -> List[Dict]:
    """Load chunks from chunks-map.json"""
    chunks_file = "chunks-map.json"

    if not os.path.exists(chunks_file):
        print(f"Error: {chunks_file} not found. Run chunking preparation first.")
        sys.exit(1)

    with open(chunks_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data['chunks']

def load_chunk_content(chunk: Dict) -> str:
    """
    Load actual content for a chunk from the markdown files
    Returns the section text from the corresponding module file
    """
    module_file_map = {
        "intro": "content/1-introduction/Introduction.md",
        "ros2": "content/2-ros2-nervous-system/Module-1-ROS2.md",
        "digital-twin": "content/3-digital-twin/Module-2-Digital-Twin.md",
        "vla": "content/4-vision-language-action/Module-4-VLA.md",
        "capstone": "content/5-capstone-autonomous-humanoid/Capstone-Guidance-Narrative.md"
    }

    module_id = chunk['module_id']
    section_num = chunk['section_number']

    file_path = module_file_map.get(module_id)
    if not file_path or not os.path.exists(file_path):
        return f"Content for {chunk['section_title']}"

    # Read the module file and extract the section content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple extraction: find section by number
    # This is a simplified approach; production code would use more robust parsing
    section_marker = f"## {section_num}."
    start_idx = content.find(section_marker)

    if start_idx == -1:
        # Try alternative format
        section_marker = f"## {section_num} "
        start_idx = content.find(section_marker)

    if start_idx == -1:
        return f"{chunk['section_title']}: {', '.join(chunk['concepts'])}"

    # Find next section or end of file
    next_section = content.find("\n## ", start_idx + 1)
    if next_section == -1:
        section_content = content[start_idx:]
    else:
        section_content = content[start_idx:next_section]

    return section_content.strip()

def generate_embedding(text: str) -> List[float]:
    """Generate embedding using OpenAI API"""
    response = openai.Embedding.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']

def create_qdrant_collection():
    """Create Qdrant collection for textbook chunks"""
    collection_name = "textbook_chunks"

    # Check if collection exists
    try:
        qdrant_client.get_collection(collection_name)
        print(f"Collection '{collection_name}' already exists. Deleting...")
        qdrant_client.delete_collection(collection_name)
    except:
        pass

    # Create new collection
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=EMBEDDING_DIMENSION, distance=Distance.COSINE)
    )

    print(f"Created collection '{collection_name}' with dimension {EMBEDDING_DIMENSION}")
    return collection_name

def upload_to_qdrant(collection_name: str, chunks: List[Dict]):
    """Upload chunks with embeddings to Qdrant"""
    points = []

    for idx, chunk in enumerate(tqdm(chunks, desc="Generating embeddings")):
        # Load actual content
        content = load_chunk_content(chunk)

        # Generate embedding
        embedding = generate_embedding(content)

        # Create point
        point = PointStruct(
            id=idx,
            vector=embedding,
            payload={
                "chunk_id": chunk['chunk_id'],
                "module": chunk['module'],
                "module_id": chunk['module_id'],
                "module_number": chunk['module_number'],
                "section_number": chunk['section_number'],
                "section_title": chunk['section_title'],
                "citation_id": chunk['citation_id'],
                "concepts": chunk['concepts'],
                "word_count": chunk['word_count'],
                "content": content[:500]  # Store first 500 chars for preview
            }
        )
        points.append(point)

    # Batch upload
    qdrant_client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"Uploaded {len(points)} chunks to Qdrant")

def store_in_postgres(chunks: List[Dict]):
    """Store chunk metadata in Postgres database"""
    conn = psycopg2.connect(NEON_DATABASE_URL)
    cur = conn.cursor()

    for idx, chunk in enumerate(tqdm(chunks, desc="Storing in Postgres")):
        # Load content
        content = load_chunk_content(chunk)

        cur.execute("""
            INSERT INTO chunks (chunk_id, module_id, module_number, section_number,
                                section_title, content, embedding_id, citation_id,
                                concepts, word_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (chunk_id) DO UPDATE SET
                content = EXCLUDED.content,
                embedding_id = EXCLUDED.embedding_id,
                updated_at = NOW()
        """, (
            chunk['chunk_id'],
            chunk['module_id'],
            chunk['module_number'],
            chunk['section_number'],
            chunk['section_title'],
            content,
            str(idx),  # Qdrant point ID
            chunk['citation_id'],
            chunk['concepts'],
            chunk['word_count']
        ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Stored {len(chunks)} chunks in Postgres")

def main():
    """Main execution function"""
    print("=" * 60)
    print("Physical AI Textbook - Embedding Generation")
    print("=" * 60)

    # Load chunks
    print("\n[1/4] Loading chunks...")
    chunks = load_chunks()
    print(f"Loaded {len(chunks)} chunks")

    # Create Qdrant collection
    print("\n[2/4] Creating Qdrant collection...")
    collection_name = create_qdrant_collection()

    # Upload to Qdrant
    print("\n[3/4] Generating embeddings and uploading to Qdrant...")
    upload_to_qdrant(collection_name, chunks)

    # Store in Postgres
    print("\n[4/4] Storing metadata in Postgres...")
    store_in_postgres(chunks)

    print("\n" + "=" * 60)
    print("✅ Embedding generation complete!")
    print("=" * 60)
    print(f"Total chunks processed: {len(chunks)}")
    print(f"Qdrant collection: {collection_name}")
    print(f"Database: Neon Postgres")

if __name__ == "__main__":
    main()

# Deployment Guide — Physical AI Textbook with RAG Tutor

**Project**: Physical AI & Humanoid Robotics — AI-Native Textbook with RAG Tutor
**Target Platform**: Docusaurus + GitHub Pages/Vercel
**RAG Backend**: FastAPI + Neon Postgres + Qdrant Cloud

---

## 📋 Prerequisites

Before deployment, ensure Phase 1 (Content Authoring) is complete:

✅ **Phase 1 Complete** (40% of project)
- All 5 modules authored and validated
- 27,687 words of content
- 100% specification compliance

---

## 🚀 Quick Start (For Running the Application)

### Option 1: Complete Phases 2-5 Manually

Follow the detailed phase-by-phase instructions below.

### Option 2: Use Automated Deployment Script (Recommended)

```bash
# Navigate to project directory
cd C:/Users/lenovo/Desktop/Hakathon_I/claude

# Run automated deployment script (if available)
./scripts/deploy-full-stack.sh

# Or run phase-by-phase
./scripts/phase2-rag-prep.sh        # RAG preparation
./scripts/phase3-rag-build.sh       # RAG system build
./scripts/phase4-integration.sh     # Integration
./scripts/phase5-deployment.sh      # Final deployment
```

---

## 📖 Phase-by-Phase Deployment Instructions

### Phase 2: RAG Knowledge Base Preparation (20% Effort, ~2 weeks)

#### Task 2.1: Normalize Markdown Structure

**Goal**: Standardize content format for RAG retrieval

```bash
# Step 1: Install markdown linting tools
npm install -g markdownlint-cli

# Step 2: Lint all content files
markdownlint content/**/*.md --fix

# Step 3: Add metadata headers to each module
# Edit each .md file to include:
---
module: introduction
id: intro
sections: 10
retrieval_ready: true
---
```

**Expected Output**: All 5 content files have consistent formatting

---

#### Task 2.2: Define Chunking Strategy

**Goal**: Break content into retrievable chunks for RAG

**Recommended Strategy**: Section-level chunking

```javascript
// chunking-config.js
export const chunkingStrategy = {
  level: "section",  // Chunk by section (## headings)
  minChunkSize: 200,  // Minimum words per chunk
  maxChunkSize: 1000, // Maximum words per chunk
  overlapSize: 50,    // Overlap between chunks
  metadata: ["module", "section", "concepts"]
};
```

**Action**:
1. Parse each module's markdown
2. Split by `##` headings
3. Create chunk IDs: `intro-sec1`, `ros2-sec2`, etc.
4. Generate chunk mapping file

**Expected Output**: `chunks-map.json` with ~50-60 chunks

---

#### Task 2.3: Create Terminology Glossary

**Goal**: Extract and define all technical terms

```bash
# Step 1: Extract technical terms from all modules
node scripts/extract-terms.js content/ > glossary-raw.json

# Step 2: Review and refine glossary
# Edit glossary-raw.json to add definitions

# Step 3: Generate cross-module term index
node scripts/build-term-index.js glossary-raw.json > term-index.json
```

**Expected Output**: `glossary.json` with 100+ technical terms

**Example Entry**:
```json
{
  "term": "Digital Twin",
  "definition": "A simulation model that mirrors a real or hypothetical robotic system",
  "modules": ["introduction", "digital-twin", "capstone"],
  "first_mention": "digital-twin-sec1"
}
```

---

#### Task 2.4: Prepare Citation Framework

**Goal**: Add citation anchors for RAG grounding

```markdown
<!-- Example: Add citation anchors to Introduction.md -->

## 1. From Digital AI to Physical AI {#intro-sec1}

<!-- Content here -->

Citation format for RAG responses:
> According to the Introduction (Section 1): "Physical AI is intelligence deployed in the physical world..." [intro-sec1]
```

**Action**:
1. Add anchor IDs to all section headings
2. Create citation template rules
3. Document grounding requirements

**Expected Output**: All sections have citation anchors; `citation-rules.md` created

---

### Phase 3: RAG System Design & Validation (15% Effort, ~1.5 weeks)

#### Task 3.1: Set Up RAG Backend Infrastructure

**Tech Stack**:
- **Vector Database**: Qdrant Cloud (free tier)
- **SQL Database**: Neon Serverless Postgres (free tier)
- **Backend**: FastAPI (Python)
- **LLM**: OpenAI GPT-4 or compatible API

**Step 1: Install Dependencies**

```bash
# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install RAG backend dependencies
pip install fastapi uvicorn openai qdrant-client psycopg2-binary python-dotenv
```

**Step 2: Configure Qdrant Cloud**

```bash
# Sign up at https://cloud.qdrant.io (free tier)
# Get API key and cluster URL

# Create .env file
QDRANT_API_KEY=your_api_key_here
QDRANT_CLUSTER_URL=https://your-cluster.qdrant.io
OPENAI_API_KEY=your_openai_key_here
NEON_DATABASE_URL=postgresql://user:pass@host/db
```

**Step 3: Set Up Neon Postgres**

```bash
# Sign up at https://neon.tech (free tier)
# Create database: physical_ai_textbook

# Run schema migration
psql $NEON_DATABASE_URL < schema.sql
```

**Schema**:
```sql
CREATE TABLE chunks (
  id SERIAL PRIMARY KEY,
  chunk_id VARCHAR(50) UNIQUE NOT NULL,
  module VARCHAR(50) NOT NULL,
  section VARCHAR(100) NOT NULL,
  content TEXT NOT NULL,
  embedding_id VARCHAR(100),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE queries (
  id SERIAL PRIMARY KEY,
  query TEXT NOT NULL,
  response TEXT NOT NULL,
  citations JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

#### Task 3.2: Generate Embeddings and Load to Qdrant

**Step 1: Generate Embeddings for All Chunks**

```python
# scripts/generate_embeddings.py
import openai
from qdrant_client import QdrantClient
import json

# Load chunks
with open('chunks-map.json', 'r') as f:
    chunks = json.load(f)

# Initialize Qdrant
client = QdrantClient(url=QDRANT_CLUSTER_URL, api_key=QDRANT_API_KEY)

# Create collection
client.create_collection(
    collection_name="textbook_chunks",
    vectors_config={"size": 1536, "distance": "Cosine"}
)

# Generate embeddings and upload
for chunk in chunks:
    embedding = openai.Embedding.create(
        input=chunk['content'],
        model="text-embedding-ada-002"
    )['data'][0]['embedding']

    client.upsert(
        collection_name="textbook_chunks",
        points=[{
            "id": chunk['id'],
            "vector": embedding,
            "payload": {
                "module": chunk['module'],
                "section": chunk['section'],
                "content": chunk['content'],
                "citation": chunk['citation_id']
            }
        }]
    )
```

**Run**:
```bash
python scripts/generate_embeddings.py
```

**Expected Output**: ~50-60 chunks uploaded to Qdrant with embeddings

---

#### Task 3.3: Build RAG FastAPI Backend

**File**: `rag_api/main.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient
import openai
import os

app = FastAPI()

# Initialize clients
qdrant = QdrantClient(url=os.getenv("QDRANT_CLUSTER_URL"), api_key=os.getenv("QDRANT_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

class Query(BaseModel):
    question: str
    top_k: int = 3

@app.post("/ask")
async def ask_question(query: Query):
    # Step 1: Generate query embedding
    query_embedding = openai.Embedding.create(
        input=query.question,
        model="text-embedding-ada-002"
    )['data'][0]['embedding']

    # Step 2: Search Qdrant for relevant chunks
    results = qdrant.search(
        collection_name="textbook_chunks",
        query_vector=query_embedding,
        limit=query.top_k
    )

    # Step 3: Build context from retrieved chunks
    context = "\n\n".join([
        f"[{r.payload['citation']}] {r.payload['content']}"
        for r in results
    ])

    # Step 4: Generate response with mandatory citations
    prompt = f"""You are a RAG tutor for a Physical AI textbook. Answer the question using ONLY the provided context. You MUST cite sources using the citation IDs provided.

Context:
{context}

Question: {query.question}

Instructions:
- Answer based ONLY on the context provided
- Include citations in your response: [citation-id]
- If the answer is not in the context, say "I can only answer based on the textbook content"
- Do NOT hallucinate or use external knowledge

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    return {
        "question": query.question,
        "answer": answer,
        "sources": [r.payload['citation'] for r in results]
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
```

**Run Backend**:
```bash
uvicorn rag_api.main:app --reload --port 8000
```

**Test**:
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is a Digital Twin?"}'
```

---

#### Task 3.4: Validate RAG with Test Queries

**Create Test Suite**: `tests/rag_validation.py`

```python
test_queries = [
    {
        "question": "What is the difference between Physical AI and digital AI?",
        "expected_citation": "intro-sec1",
        "module": "introduction"
    },
    {
        "question": "Explain ROS 2 communication patterns",
        "expected_citation": "ros2-sec3",
        "module": "ros2"
    },
    {
        "question": "What is the reality gap?",
        "expected_citation": "digital-twin-sec2",
        "module": "digital-twin"
    },
    # Add 47+ more test queries...
]

# Run validation
for test in test_queries:
    response = ask_question(test['question'])
    assert test['expected_citation'] in response['sources'], f"Failed: {test['question']}"
    assert "I can only answer" not in response['answer'], f"Refused valid query: {test['question']}"
```

**Expected Output**: 100% test pass rate with mandatory citations

---

### Phase 4: Integration & Docusaurus Deployment (15% Effort, ~1.5 weeks)

#### Task 4.1: Set Up Docusaurus

```bash
# Step 1: Install Docusaurus
npx create-docusaurus@latest physical-ai-textbook classic

cd physical-ai-textbook

# Step 2: Configure Docusaurus
# Edit docusaurus.config.js
```

**Docusaurus Config**:
```javascript
module.exports = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'An AI-Native Textbook with Embedded RAG Tutor',
  url: 'https://your-username.github.io',
  baseUrl: '/physical-ai-textbook/',
  organizationName: 'your-username',
  projectName: 'physical-ai-textbook',

  themeConfig: {
    navbar: {
      title: 'Physical AI',
      items: [
        {to: '/docs/intro', label: 'Introduction', position: 'left'},
        {to: '/docs/ros2', label: 'ROS 2', position: 'left'},
        {to: '/docs/digital-twin', label: 'Digital Twin', position: 'left'},
        {to: '/docs/vla', label: 'VLA', position: 'left'},
        {to: '/docs/capstone', label: 'Capstone', position: 'left'},
      ],
    },
  },
};
```

---

#### Task 4.2: Import Content to Docusaurus

```bash
# Copy content files to Docusaurus docs folder
cp content/1-introduction/Introduction.md physical-ai-textbook/docs/intro.md
cp content/2-ros2-nervous-system/Module-1-ROS2.md physical-ai-textbook/docs/ros2.md
cp content/3-digital-twin/Module-2-Digital-Twin.md physical-ai-textbook/docs/digital-twin.md
cp content/4-vision-language-action/Module-4-VLA.md physical-ai-textbook/docs/vla.md
cp content/5-capstone-autonomous-humanoid/Capstone-Guidance-Narrative.md physical-ai-textbook/docs/capstone.md
```

---

#### Task 4.3: Embed RAG Chatbot in Docusaurus

**Create React Component**: `src/components/RAGChat.js`

```javascript
import React, { useState } from 'react';

export default function RAGChat() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    setLoading(true);
    const res = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: query })
    });
    const data = await res.json();
    setResponse(data);
    setLoading(false);
  };

  return (
    <div className="rag-chat">
      <h3>Ask the RAG Tutor</h3>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question about the textbook..."
      />
      <button onClick={askQuestion} disabled={loading}>
        {loading ? 'Thinking...' : 'Ask'}
      </button>

      {response && (
        <div className="response">
          <p><strong>Answer:</strong> {response.answer}</p>
          <p><strong>Sources:</strong> {response.sources.join(', ')}</p>
        </div>
      )}
    </div>
  );
}
```

**Import in Docusaurus pages**:
```javascript
import RAGChat from '@site/src/components/RAGChat';

<RAGChat />
```

---

#### Task 4.4: Deploy to GitHub Pages

```bash
# Step 1: Build Docusaurus
cd physical-ai-textbook
npm run build

# Step 2: Deploy to GitHub Pages
GIT_USER=your-username npm run deploy
```

**Expected Output**: Textbook live at `https://your-username.github.io/physical-ai-textbook/`

---

### Phase 5: Final Review & Submission (10% Effort, ~1 week)

#### Task 5.1: Create Demo Video (≤90 seconds)

**Script**:
1. Show textbook landing page (5 sec)
2. Navigate through modules (15 sec)
3. Demonstrate RAG chatbot:
   - Ask: "What is a Digital Twin?" (20 sec)
   - Show citation in response (10 sec)
   - Ask: "How does VLA replanning work?" (20 sec)
   - Show grounded answer (10 sec)
4. Show capstone architecture diagram (10 sec)

**Tools**: OBS Studio, Loom, or similar

---

#### Task 5.2: Create README and Documentation

**README.md**:
```markdown
# Physical AI & Humanoid Robotics — AI-Native Textbook

An AI-native textbook with embedded RAG tutor for teaching Physical AI.

## Features
- 5 comprehensive modules (27,687 words)
- RAG chatbot with mandatory citations
- Docusaurus-powered web platform
- Constitutional compliance (AI-native, spec-driven)

## Live Demo
https://your-username.github.io/physical-ai-textbook/

## Tech Stack
- Content: Spec-Kit Plus + Claude Code
- Publishing: Docusaurus
- RAG: FastAPI + Qdrant + Neon Postgres + OpenAI

## Installation
See DEPLOYMENT_GUIDE.md
```

---

#### Task 5.3: Submit to Hackathon

**Submission Checklist**:
- [x] GitHub repository public
- [x] Live textbook URL
- [x] Demo video (≤90 seconds)
- [x] README with features
- [x] RAG chatbot working with citations
- [x] All Hackathon-1 requirements satisfied

**Submit to**: [Hackathon platform URL]

---

## 🎯 Summary

To **run the application**, complete Phases 2-5:

1. **Phase 2**: Prepare content for RAG (~2 weeks)
2. **Phase 3**: Build RAG chatbot (~1.5 weeks)
3. **Phase 4**: Deploy to Docusaurus + GitHub Pages (~1.5 weeks)
4. **Phase 5**: Final review and submission (~1 week)

**Total Time**: 6-7 weeks (with AI acceleration: ~3-4 weeks)

**Current Status**: Phase 1 complete (40%). Ready to start Phase 2.

---

**Questions?** Refer to PROJECT_STATUS.md for detailed phase breakdown.

"""
RAG FastAPI Backend
Physical AI Textbook RAG System - Phase 3 Task 3.3

This FastAPI server provides:
- /ask endpoint for RAG-based question answering
- /health endpoint for health checks
- Mandatory citation enforcement
- Grounding validation
"""

import os
import time
from typing import List, Dict, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient
import openai
import psycopg2
from psycopg2.extras import Json

# Import demo mode content search
from content_search import demo_ask

# Import authentication system
from auth import (
    SessionManager,
    authenticate_user,
    get_session_from_request,
    require_auth,
    rate_limit,
    SESSION_COOKIE_NAME
)

# Import Gemini RAG system
from gemini_rag import gemini_rag_ask

# Load environment variables
load_dotenv()

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_URL = os.getenv("QDRANT_CLUSTER_URL")
NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL")
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "500"))
RAG_TOP_K = int(os.getenv("RAG_TOP_K", "3"))
RAG_MIN_CONFIDENCE = float(os.getenv("RAG_MIN_CONFIDENCE", "0.7"))

# Initialize clients
openai.api_key = OPENAI_API_KEY
qdrant_client = QdrantClient(url=QDRANT_CLUSTER_URL, api_key=QDRANT_API_KEY)

# Initialize FastAPI app
app = FastAPI(
    title="Physical AI Textbook RAG API",
    description="RAG-based Q&A system with mandatory citation grounding",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class Query(BaseModel):
    question: str = Field(..., min_length=3, max_length=500, description="User's question")
    top_k: int = Field(RAG_TOP_K, ge=1, le=10, description="Number of chunks to retrieve")
    min_confidence: float = Field(RAG_MIN_CONFIDENCE, ge=0.0, le=1.0, description="Minimum similarity score")

class Source(BaseModel):
    citation_id: str
    module: str
    section_title: str
    confidence: float

class Answer(BaseModel):
    question: str
    answer: str
    sources: List[Source]
    execution_time_ms: int
    model: str

# Authentication Models
class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=100)

class LoginResponse(BaseModel):
    authenticated: bool
    user_id: str

class AuthStatus(BaseModel):
    authenticated: bool
    user_id: Optional[str] = None

# RAG System Prompt
SYSTEM_PROMPT = """You are a RAG tutor for the Physical AI & Humanoid Robotics textbook.

Your purpose is to help learners understand concepts from the textbook by answering questions using ONLY the provided context from the textbook.

MANDATORY RULES:
1. Answer questions using ONLY the context provided
2. Include citations using the format [citation-id]
3. If the answer is not in the context, say: "I can only answer based on the textbook content. This topic is not covered."
4. Do NOT hallucinate or use external knowledge
5. Do NOT speculate beyond what the textbook says
6. Do NOT provide personal opinions

Citation format examples:
- "ROS 2 is middleware [ros2-sec1]"
- "Digital twins mirror real robots [digital-twin-sec1, capstone-sec3]"
- "VLA integrates vision, language, and action [vla-sec1]"
"""

def generate_embedding(text: str) -> List[float]:
    """Generate embedding for query using OpenAI"""
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

def search_similar_chunks(query_embedding: List[float], top_k: int, min_confidence: float) -> List[Dict]:
    """Search Qdrant for similar chunks"""
    results = qdrant_client.search(
        collection_name="textbook_chunks",
        query_vector=query_embedding,
        limit=top_k
    )

    # Filter by confidence and format results
    chunks = []
    for result in results:
        if result.score >= min_confidence:
            chunks.append({
                "citation_id": result.payload['citation_id'],
                "module": result.payload['module'],
                "module_id": result.payload['module_id'],
                "section_title": result.payload['section_title'],
                "content": result.payload.get('content', ''),
                "concepts": result.payload.get('concepts', []),
                "confidence": result.score
            })

    return chunks

def build_context(chunks: List[Dict]) -> str:
    """Build context string from retrieved chunks"""
    context_parts = []

    for chunk in chunks:
        context_parts.append(f"[{chunk['citation_id']}] {chunk['section_title']}")
        context_parts.append(chunk['content'])
        context_parts.append("")  # Blank line separator

    return "\n".join(context_parts)

def generate_rag_response(question: str, context: str) -> str:
    """Generate response using GPT-4 with mandatory citations"""
    prompt = f"""Context from Physical AI Textbook:
{context}

Question: {question}

Instructions:
- Answer based ONLY on the context provided above
- Include citations in your response using the format [citation-id]
- If the answer is not in the context, say "I can only answer based on the textbook content. This topic is not covered."
- Do NOT hallucinate or use external knowledge
- Be concise but complete

Answer:"""

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS
    )

    return response.choices[0].message.content.strip()

def log_query_to_db(question: str, answer: str, sources: List[Source], execution_time_ms: int):
    """Log query and response to Postgres for analytics"""
    try:
        conn = psycopg2.connect(NEON_DATABASE_URL)
        cur = conn.cursor()

        citations = [source.citation_id for source in sources]

        cur.execute("""
            INSERT INTO queries (query, response, citations, top_k, min_confidence,
                                chunks_retrieved, execution_time_ms)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            question,
            answer,
            Json(citations),
            RAG_TOP_K,
            RAG_MIN_CONFIDENCE,
            len(sources),
            execution_time_ms
        ))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error logging to database: {e}")

# ============================================================================
# AUTHENTICATION ENDPOINTS
# ============================================================================

@app.post("/auth/login", response_model=LoginResponse)
async def login(credentials: LoginRequest, response: Response):
    """
    Authenticate user and create session

    Returns session cookie on success
    """
    user_id = authenticate_user(credentials.username, credentials.password)

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create session
    session_id = SessionManager.create_session(user_id)

    # Set secure cookie
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=session_id,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=24 * 60 * 60  # 24 hours
    )

    return LoginResponse(authenticated=True, user_id=user_id)


@app.post("/auth/logout")
async def logout(request: Request, response: Response):
    """Destroy session and clear cookie"""
    session_id = request.cookies.get(SESSION_COOKIE_NAME)

    if session_id:
        SessionManager.destroy_session(session_id)

    response.delete_cookie(SESSION_COOKIE_NAME)

    return {"message": "Logged out successfully"}


@app.get("/auth/status", response_model=AuthStatus)
async def auth_status(request: Request):
    """Check authentication status"""
    session = get_session_from_request(request)

    if session:
        return AuthStatus(authenticated=True, user_id=session["user_id"])

    return AuthStatus(authenticated=False, user_id=None)


# ============================================================================
# CHATBOT ENDPOINTS
# ============================================================================

@app.post("/chat", response_model=Answer)
@require_auth
@rate_limit
async def authenticated_chat(query: Query, request: Request):
    """
    Authenticated chatbot endpoint using Gemini RAG

    Requires:
    - Valid session (authenticated user)
    - Within rate limits (20 requests per 15 minutes)

    Returns:
    - AI-generated answer grounded in textbook content
    - Citations to source material
    """
    start_time = time.time()

    try:
        # Use Gemini RAG pipeline
        result = gemini_rag_ask(query.question)

        execution_time_ms = int((time.time() - start_time) * 1000)

        # Format sources
        sources = [
            Source(
                citation_id=s['citation_id'],
                module=s['module'],
                section_title=s['section_title'],
                confidence=s['confidence']
            )
            for s in result.get('sources', [])
        ]

        return Answer(
            question=query.question,
            answer=result['answer'],
            sources=sources,
            execution_time_ms=execution_time_ms,
            model=result['model']
        )

    except Exception as e:
        error_msg = str(e)

        # Handle specific error types
        if "quota" in error_msg.lower():
            raise HTTPException(
                status_code=503,
                detail="Chatbot temporarily unavailable due to quota limits. Please try again later."
            )
        elif "timeout" in error_msg.lower():
            raise HTTPException(
                status_code=504,
                detail="Request timed out. Please try a shorter question."
            )
        elif "configuration" in error_msg.lower() or "key" in error_msg.lower():
            raise HTTPException(
                status_code=500,
                detail="Chatbot configuration error. Please contact support."
            )
        else:
            raise HTTPException(
                status_code=503,
                detail=f"Unable to process request: {error_msg}"
            )


@app.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    """
    Ask a question to the RAG tutor

    Returns an answer grounded in textbook content with mandatory citations
    """
    start_time = time.time()

    # Check if we should use demo mode (invalid API keys)
    use_demo_mode = False
    if not OPENAI_API_KEY or OPENAI_API_KEY.startswith("REPLACE_") or OPENAI_API_KEY.startswith("your_"):
        use_demo_mode = True

    if use_demo_mode:
        # Use demo mode - direct content search without external APIs
        try:
            result = demo_ask(query.question)
            execution_time_ms = int((time.time() - start_time) * 1000)

            sources = [
                Source(
                    citation_id=s['citation_id'],
                    module=s['module'],
                    section_title=s['section_title'],
                    confidence=s['confidence']
                )
                for s in result.get('sources', [])
            ]

            return Answer(
                question=query.question,
                answer=result['answer'],
                sources=sources,
                execution_time_ms=execution_time_ms,
                model="demo-mode (direct content search)"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Demo mode error: {str(e)}")

    # Full RAG mode with OpenAI
    try:
        # Step 1: Generate query embedding
        query_embedding = generate_embedding(query.question)

        # Step 2: Search for similar chunks
        chunks = search_similar_chunks(query_embedding, query.top_k, query.min_confidence)

        if not chunks:
            # No relevant chunks found
            return Answer(
                question=query.question,
                answer="I can only answer based on the textbook content. This topic is not covered in the course material.",
                sources=[],
                execution_time_ms=int((time.time() - start_time) * 1000),
                model=LLM_MODEL
            )

        # Step 3: Build context
        context = build_context(chunks)

        # Step 4: Generate RAG response
        answer = generate_rag_response(query.question, context)

        # Step 5: Format sources
        sources = [
            Source(
                citation_id=chunk['citation_id'],
                module=chunk['module'],
                section_title=chunk['section_title'],
                confidence=chunk['confidence']
            )
            for chunk in chunks
        ]

        execution_time_ms = int((time.time() - start_time) * 1000)

        # Step 6: Log query
        log_query_to_db(query.question, answer, sources, execution_time_ms)

        return Answer(
            question=query.question,
            answer=answer,
            sources=sources,
            execution_time_ms=execution_time_ms,
            model=LLM_MODEL
        )

    except Exception as e:
        # If RAG fails, fall back to demo mode
        try:
            result = demo_ask(query.question)
            execution_time_ms = int((time.time() - start_time) * 1000)

            sources = [
                Source(
                    citation_id=s['citation_id'],
                    module=s['module'],
                    section_title=s['section_title'],
                    confidence=s['confidence']
                )
                for s in result.get('sources', [])
            ]

            return Answer(
                question=query.question,
                answer=result['answer'] + "\n\n(Fallback to demo mode due to API error)",
                sources=sources,
                execution_time_ms=execution_time_ms,
                model="demo-mode (fallback)"
            )
        except:
            raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        # Test Qdrant connection
        qdrant_client.get_collection("textbook_chunks")
        qdrant_status = "ok"
    except Exception as e:
        qdrant_status = f"error: {str(e)}"

    try:
        # Test Postgres connection
        conn = psycopg2.connect(NEON_DATABASE_URL)
        conn.close()
        postgres_status = "ok"
    except Exception as e:
        postgres_status = f"error: {str(e)}"

    return {
        "status": "ok" if qdrant_status == "ok" and postgres_status == "ok" else "degraded",
        "qdrant": qdrant_status,
        "postgres": postgres_status,
        "model": LLM_MODEL
    }

@app.get("/stats")
async def get_stats():
    """Get RAG system statistics"""
    try:
        conn = psycopg2.connect(NEON_DATABASE_URL)
        cur = conn.cursor()

        # Total queries
        cur.execute("SELECT COUNT(*) FROM queries")
        total_queries = cur.fetchone()[0]

        # Average execution time
        cur.execute("SELECT AVG(execution_time_ms) FROM queries")
        avg_time = cur.fetchone()[0] or 0

        # Total chunks
        cur.execute("SELECT COUNT(*) FROM chunks")
        total_chunks = cur.fetchone()[0]

        cur.close()
        conn.close()

        return {
            "total_queries": total_queries,
            "avg_execution_time_ms": round(avg_time, 2),
            "total_chunks": total_chunks,
            "collection": "textbook_chunks"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stats: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=API_PORT)

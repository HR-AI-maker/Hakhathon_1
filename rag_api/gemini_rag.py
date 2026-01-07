"""
Gemini RAG Integration
Handles RAG-based question answering using Google Gemini API
"""

import os
from typing import List, Dict, Optional

# Optional import for Gemini (gracefully handle if not available)
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None

try:
    from .content_search import search_content
except ImportError:
    from content_search import search_content

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GENAI_AVAILABLE and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Gemini model configuration
MODEL_NAME = "gemini-1.5-flash"
GENERATION_CONFIG = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


def build_rag_prompt(question: str, sources: List[Dict]) -> str:
    """Build RAG prompt with retrieved context"""

    # Build context from sources
    context_parts = []
    for source in sources:
        context_parts.append(f"[{source['citation_id']}] {source['section_title']}")
        context_parts.append(source.get('full_content', source.get('content', '')))
        context_parts.append("")  # Blank line

    context = "\n".join(context_parts)

    prompt = f"""You are a RAG tutor for the Physical AI & Humanoid Robotics textbook.

CONTEXT FROM TEXTBOOK:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
- Answer ONLY using the context provided above
- Include citations in your response using the format [citation-id]
- If the answer is not in the context, say: "I can only answer based on the textbook content. This topic is not covered."
- Do NOT use external knowledge beyond the provided context
- Do NOT speculate or make assumptions
- Be concise, educational, and accurate
- Always cite your sources

ANSWER:"""

    return prompt


def generate_with_gemini(question: str, sources: List[Dict]) -> tuple[str, str]:
    """
    Generate answer using Gemini API with RAG context

    Returns: (answer: str, model: str)
    Raises: Exception on API failures
    """

    if not GENAI_AVAILABLE:
        raise ValueError("Google Generative AI package not available")

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not configured")

    # Build prompt
    prompt = build_rag_prompt(question, sources)

    try:
        # Initialize model
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )

        # Generate response
        response = model.generate_content(prompt)

        # Extract text
        if response.text:
            return response.text.strip(), MODEL_NAME
        else:
            # Handle blocked responses
            if response.prompt_feedback:
                raise Exception(f"Content blocked: {response.prompt_feedback}")
            raise Exception("No response generated")

    except Exception as e:
        error_msg = str(e)

        # Handle specific errors
        if "quota" in error_msg.lower() or "429" in error_msg:
            raise Exception("Gemini API quota exceeded. Please try again later.")
        elif "invalid" in error_msg.lower() and "key" in error_msg.lower():
            raise Exception("Gemini API key configuration error.")
        elif "timeout" in error_msg.lower():
            raise Exception("Request timed out. Please try a shorter question.")
        else:
            raise Exception(f"Gemini API error: {error_msg}")


def gemini_rag_ask(question: str) -> Dict:
    """
    Complete RAG pipeline with Gemini

    1. Search content for relevant chunks
    2. Build RAG prompt with context
    3. Generate answer with Gemini
    4. Return structured response

    Returns dict with: question, answer, sources, model
    """

    # Step 1: Retrieve relevant content
    sources = search_content(question)

    if not sources:
        return {
            "question": question,
            "answer": "I can only answer questions based on the Physical AI & Humanoid Robotics textbook. Please ask about topics like Physical AI, ROS 2, Digital Twins, Vision-Language-Action, or the Autonomous Humanoid capstone project.",
            "sources": [],
            "model": "gemini-rag (no sources found)"
        }

    # Step 2: Generate answer with Gemini
    try:
        answer, model = generate_with_gemini(question, sources)

        # Format sources for response
        formatted_sources = [
            {
                "citation_id": s["citation_id"],
                "module": s["module"],
                "section_title": s["section_title"],
                "confidence": s["confidence"]
            }
            for s in sources[:3]  # Top 3 sources
        ]

        return {
            "question": question,
            "answer": answer,
            "sources": formatted_sources,
            "model": f"gemini-rag ({model})"
        }

    except Exception as e:
        # On Gemini failure, return error
        raise e

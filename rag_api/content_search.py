"""
Content Search Module - Demo Mode
Searches directly through textbook markdown files without requiring external APIs
"""

import os
import re
from typing import List, Dict, Tuple

# Module information
MODULES = {
    "intro": {
        "name": "Introduction",
        "file": "../content/1-introduction/Introduction.md",
        "topics": ["physical ai", "embodied intelligence", "humanoid robots", "digital twin", "simulation"]
    },
    "ros2": {
        "name": "Module 1: ROS 2",
        "file": "../content/2-ros2-nervous-system/Module-1-ROS2.md",
        "topics": ["ros 2", "ros2", "middleware", "nodes", "topics", "services", "urdf", "robotic nervous system"]
    },
    "digital-twin": {
        "name": "Module 2: Digital Twin",
        "file": "../content/3-digital-twin/Module-2-Digital-Twin.md",
        "topics": ["digital twin", "simulation", "gazebo", "physics", "reality gap", "sensor noise"]
    },
    "vla": {
        "name": "Module 4: Vision-Language-Action",
        "file": "../content/4-vision-language-action/Module-4-VLA.md",
        "topics": ["vla", "vision language action", "cognitive", "perception", "planning", "reasoning"]
    },
    "capstone": {
        "name": "Capstone: Autonomous Humanoid",
        "file": "../content/5-capstone-autonomous-humanoid/Capstone-Guidance-Narrative.md",
        "topics": ["capstone", "autonomous", "humanoid", "integration", "four-agent", "architecture"]
    }
}

def load_content(file_path: str) -> str:
    """Load content from markdown file"""
    try:
        # Adjust path relative to rag_api directory
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return ""

def extract_sections(content: str) -> List[Dict[str, str]]:
    """Extract sections from markdown content"""
    sections = []

    # Split by headers (##)
    lines = content.split('\n')
    current_section = {"title": "", "content": ""}

    for line in lines:
        if line.startswith('## '):
            # Save previous section if it has content
            if current_section["title"] and current_section["content"].strip():
                sections.append(current_section.copy())
            # Start new section
            current_section = {"title": line.replace('## ', '').strip(), "content": ""}
        elif line.startswith('# ') and not current_section["title"]:
            # Main title
            current_section["title"] = line.replace('# ', '').strip()
        else:
            current_section["content"] += line + "\n"

    # Add last section
    if current_section["title"] and current_section["content"].strip():
        sections.append(current_section)

    return sections

def search_content(query: str) -> List[Dict]:
    """Search through all textbook content"""
    query_lower = query.lower()
    results = []

    # Extract key terms from query
    query_terms = set(re.findall(r'\b\w+\b', query_lower))

    for module_id, module_info in MODULES.items():
        content = load_content(module_info["file"])
        if not content:
            continue

        sections = extract_sections(content)

        for section in sections:
            section_lower = (section["title"] + " " + section["content"]).lower()

            # Calculate relevance score
            score = 0

            # Check if any module topics match
            for topic in module_info["topics"]:
                if topic in query_lower:
                    score += 10

            # Check term matches in section
            matched_terms = sum(1 for term in query_terms if term in section_lower)
            score += matched_terms

            # Check for exact phrase match
            if query_lower in section_lower:
                score += 20

            if score > 0:
                # Get a relevant excerpt (first 500 chars of content)
                excerpt = section["content"].strip()[:500]
                if len(section["content"]) > 500:
                    excerpt += "..."

                results.append({
                    "module": module_info["name"],
                    "module_id": module_id,
                    "section_title": section["title"],
                    "content": excerpt,
                    "full_content": section["content"].strip(),
                    "confidence": min(score / 20.0, 0.99),  # Normalize score to 0-1
                    "citation_id": f"{module_id}-{section['title'][:20].lower().replace(' ', '-')}"
                })

    # Sort by confidence and return top results
    results.sort(key=lambda x: x["confidence"], reverse=True)
    return results[:5]

def generate_answer(query: str, sources: List[Dict]) -> str:
    """Generate answer from sources"""
    if not sources:
        return "I can only answer questions based on the Physical AI & Humanoid Robotics textbook. This topic doesn't appear to be covered in the available modules."

    # Build answer from top source
    top_source = sources[0]

    # Get relevant content snippet
    content = top_source["full_content"]

    # Extract most relevant paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    query_lower = query.lower()

    # Find paragraphs that match query terms
    relevant_paras = []
    for para in paragraphs:
        para_lower = para.lower()
        if any(term in para_lower for term in query_lower.split() if len(term) > 3):
            relevant_paras.append(para)
            if len(relevant_paras) >= 2:  # Get up to 2 relevant paragraphs
                break

    if not relevant_paras:
        relevant_paras = paragraphs[:2]  # Fallback to first 2 paragraphs

    # Build answer with citations
    answer = "\n\n".join(relevant_paras)

    # Add citation
    answer += f"\n\n[{top_source['citation_id']}]"

    # Limit length
    if len(answer) > 800:
        answer = answer[:800] + f"...\n\n[{top_source['citation_id']}]"

    return answer

def demo_ask(question: str) -> Dict:
    """Demo mode ask function - works without external APIs"""
    try:
        # Search content
        sources = search_content(question)

        if not sources:
            return {
                "question": question,
                "answer": "I can only answer questions based on the Physical AI & Humanoid Robotics textbook. Please ask about topics like Physical AI, ROS 2, Digital Twins, Vision-Language-Action, or the Autonomous Humanoid capstone project.",
                "sources": [],
                "mode": "demo"
            }

        # Generate answer
        answer = generate_answer(question, sources)

        # Format sources for response
        formatted_sources = [
            {
                "citation_id": s["citation_id"],
                "module": s["module"],
                "section_title": s["section_title"],
                "confidence": s["confidence"]
            }
            for s in sources[:3]
        ]

        return {
            "question": question,
            "answer": answer,
            "sources": formatted_sources,
            "mode": "demo"
        }

    except Exception as e:
        return {
            "question": question,
            "answer": f"Error processing question: {str(e)}",
            "sources": [],
            "mode": "demo"
        }

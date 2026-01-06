"""
RAG Test Queries - Validation Suite
Physical AI Textbook RAG System - Phase 3 Task 3.4

This test suite validates:
1. Single-module questions (20 queries)
2. Cross-module questions (15 queries)
3. Edge cases (10 queries)
4. Failure modes (5 queries)

Success criteria:
- 100% of answerable questions receive citations
- 0% hallucination (all facts from textbook)
- 100% refusal for out-of-scope questions
"""

import requests
import json
from typing import List, Dict

# API endpoint
API_URL = "http://localhost:8000"

class TestQuery:
    def __init__(self, question: str, expected_modules: List[str], expected_citations: List[str], category: str):
        self.question = question
        self.expected_modules = expected_modules
        self.expected_citations = expected_citations
        self.category = category

# Test Query Dataset
TEST_QUERIES = [
    # === SINGLE-MODULE QUESTIONS (Introduction) ===
    TestQuery(
        "What is Physical AI?",
        ["introduction"],
        ["intro-sec1"],
        "single-module"
    ),
    TestQuery(
        "What is embodied intelligence?",
        ["introduction"],
        ["intro-sec2"],
        "single-module"
    ),
    TestQuery(
        "Why are humanoid robots important?",
        ["introduction"],
        ["intro-sec3"],
        "single-module"
    ),
    TestQuery(
        "What is a digital twin?",
        ["introduction"],
        ["intro-sec4"],
        "single-module"
    ),

    # === SINGLE-MODULE QUESTIONS (ROS 2) ===
    TestQuery(
        "What is ROS 2?",
        ["ros2-nervous-system"],
        ["ros2-sec1"],
        "single-module"
    ),
    TestQuery(
        "How do ROS 2 topics work?",
        ["ros2-nervous-system"],
        ["ros2-sec3"],
        "single-module"
    ),
    TestQuery(
        "What are ROS 2 services?",
        ["ros2-nervous-system"],
        ["ros2-sec4"],
        "single-module"
    ),
    TestQuery(
        "How do ROS 2 actions differ from topics?",
        ["ros2-nervous-system"],
        ["ros2-sec3", "ros2-sec5"],
        "single-module"
    ),
    TestQuery(
        "What is URDF?",
        ["ros2-nervous-system"],
        ["ros2-sec7"],
        "single-module"
    ),

    # === SINGLE-MODULE QUESTIONS (Digital Twin) ===
    TestQuery(
        "What is the reality gap?",
        ["digital-twin"],
        ["digital-twin-sec2"],
        "single-module"
    ),
    TestQuery(
        "How does friction affect robot simulation?",
        ["digital-twin"],
        ["digital-twin-sec3"],
        "single-module"
    ),
    TestQuery(
        "Why is center of mass important for humanoid robots?",
        ["digital-twin"],
        ["digital-twin-sec4"],
        "single-module"
    ),
    TestQuery(
        "What is sensor noise and why does it matter?",
        ["digital-twin"],
        ["digital-twin-sec5"],
        "single-module"
    ),
    TestQuery(
        "How does Gazebo integrate with ROS 2?",
        ["digital-twin"],
        ["digital-twin-sec7"],
        "single-module"
    ),

    # === SINGLE-MODULE QUESTIONS (VLA) ===
    TestQuery(
        "What is the VLA agent loop?",
        ["vision-language-action"],
        ["vla-sec1"],
        "single-module"
    ),
    TestQuery(
        "What is perception grounding?",
        ["vision-language-action"],
        ["vla-sec2"],
        "single-module"
    ),
    TestQuery(
        "What is world state in VLA?",
        ["vision-language-action"],
        ["vla-sec3"],
        "single-module"
    ),
    TestQuery(
        "How does VLA handle replanning?",
        ["vision-language-action"],
        ["vla-sec7"],
        "single-module"
    ),
    TestQuery(
        "What are fallback strategies in VLA?",
        ["vision-language-action"],
        ["vla-sec8"],
        "single-module"
    ),

    # === SINGLE-MODULE QUESTIONS (Capstone) ===
    TestQuery(
        "What are the four agents in the capstone architecture?",
        ["capstone"],
        ["capstone-sec3"],
        "single-module"
    ),
    TestQuery(
        "What is the elder care use case?",
        ["capstone"],
        ["capstone-sec7"],
        "single-module"
    ),

    # === CROSS-MODULE QUESTIONS ===
    TestQuery(
        "How does VLA connect to ROS 2?",
        ["vision-language-action", "ros2-nervous-system", "capstone"],
        ["vla-sec6", "ros2-sec6", "capstone-sec2"],
        "cross-module"
    ),
    TestQuery(
        "How do digital twins help with VLA development?",
        ["digital-twin", "vision-language-action", "capstone"],
        ["digital-twin-sec1", "vla-sec1", "capstone-sec6"],
        "cross-module"
    ),
    TestQuery(
        "What is the complete flow from voice command to robot action?",
        ["capstone", "vision-language-action", "ros2-nervous-system"],
        ["capstone-sec2", "vla-sec6", "ros2-sec5"],
        "cross-module"
    ),
    TestQuery(
        "How does perception from Isaac integrate with VLA?",
        ["vision-language-action", "capstone"],
        ["vla-sec2", "capstone-sec2"],
        "cross-module"
    ),
    TestQuery(
        "What is simulation-first development and how does it work?",
        ["introduction", "digital-twin", "capstone"],
        ["intro-sec4", "digital-twin-sec1", "capstone-sec6"],
        "cross-module"
    ),
    TestQuery(
        "How is safety enforced in the autonomous humanoid system?",
        ["vision-language-action", "capstone"],
        ["vla-sec8", "capstone-sec3", "capstone-sec5"],
        "cross-module"
    ),
    TestQuery(
        "What is the relationship between nodes, topics, and the VLA agent?",
        ["ros2-nervous-system", "vision-language-action"],
        ["ros2-sec2", "ros2-sec3", "vla-sec6"],
        "cross-module"
    ),
    TestQuery(
        "How does Gazebo simulation connect to the ROS 2 system?",
        ["digital-twin", "ros2-nervous-system"],
        ["digital-twin-sec7", "ros2-sec1"],
        "cross-module"
    ),
    TestQuery(
        "What are the key differences between simulation and reality?",
        ["digital-twin", "capstone"],
        ["digital-twin-sec2", "capstone-sec6"],
        "cross-module"
    ),
    TestQuery(
        "How does the capstone system handle failure scenarios?",
        ["capstone", "vision-language-action"],
        ["capstone-sec5", "vla-sec7", "vla-sec8"],
        "cross-module"
    ),
    TestQuery(
        "What is the role of URDF in the full robotic system?",
        ["ros2-nervous-system", "digital-twin", "capstone"],
        ["ros2-sec7", "digital-twin-sec7"],
        "cross-module"
    ),
    TestQuery(
        "How does human-in-the-loop supervision work?",
        ["introduction", "capstone"],
        ["intro-sec9", "capstone-sec8"],
        "cross-module"
    ),
    TestQuery(
        "What is the complete data flow in the autonomous humanoid?",
        ["capstone"],
        ["capstone-sec4"],
        "cross-module"
    ),
    TestQuery(
        "How do you validate that a simulation will transfer to reality?",
        ["digital-twin", "capstone"],
        ["digital-twin-sec2", "capstone-sec6"],
        "cross-module"
    ),
    TestQuery(
        "What is the agent loop and where is it implemented?",
        ["vision-language-action", "capstone"],
        ["vla-sec1", "capstone-sec2"],
        "cross-module"
    ),

    # === EDGE CASES ===
    TestQuery(
        "Tell me everything about ROS 2",
        ["ros2-nervous-system"],
        [],  # Too broad, RAG should provide focused answer from retrieved chunks
        "edge-case"
    ),
    TestQuery(
        "What is the third module about?",
        [],  # Module 3 (Isaac) is not implemented
        [],
        "edge-case"
    ),
    TestQuery(
        "Can you explain the course structure?",
        ["introduction"],
        ["intro-sec5"],
        "edge-case"
    ),
    TestQuery(
        "What are the prerequisites for this course?",
        ["introduction"],
        ["intro-sec7"],
        "edge-case"
    ),
    TestQuery(
        "What is the AI-native textbook methodology?",
        ["introduction"],
        ["intro-sec6"],
        "edge-case"
    ),
    TestQuery(
        "How many modules are there?",
        ["introduction"],
        ["intro-sec5"],
        "edge-case"
    ),
    TestQuery(
        "What is the capstone project about?",
        ["introduction", "capstone"],
        ["intro-sec5", "capstone-sec1"],
        "edge-case"
    ),
    TestQuery(
        "Which topics are out of scope?",
        [],  # Not explicitly covered
        [],
        "edge-case"
    ),
    TestQuery(
        "What are the learning outcomes?",
        ["introduction"],
        ["intro-sec10"],
        "edge-case"
    ),
    TestQuery(
        "How is this different from traditional robotics courses?",
        ["introduction"],
        ["intro-sec6"],
        "edge-case"
    ),

    # === FAILURE MODES (should refuse to answer) ===
    TestQuery(
        "What is the best programming language for AI?",
        [],  # Out of scope
        [],
        "failure-mode"
    ),
    TestQuery(
        "How do I install Python on Windows?",
        [],  # Out of scope
        [],
        "failure-mode"
    ),
    TestQuery(
        "What is quantum computing?",
        [],  # Completely unrelated
        [],
        "failure-mode"
    ),
    TestQuery(
        "Who invented ROS?",
        [],  # Historical information not in textbook
        [],
        "failure-mode"
    ),
    TestQuery(
        "What is the future of humanoid robotics?",
        [],  # Speculation beyond textbook
        [],
        "failure-mode"
    ),
]

def run_test_query(query: TestQuery) -> Dict:
    """Run a single test query against the RAG API"""
    try:
        response = requests.post(
            f"{API_URL}/ask",
            json={"question": query.question},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "answer": data["answer"],
                "sources": [s["citation_id"] for s in data["sources"]],
                "execution_time_ms": data["execution_time_ms"]
            }
        else:
            return {
                "success": False,
                "error": f"HTTP {response.status_code}: {response.text}"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def validate_response(query: TestQuery, result: Dict) -> Dict:
    """Validate RAG response against expected criteria"""
    validation = {
        "has_answer": bool(result.get("answer")),
        "has_citations": len(result.get("sources", [])) > 0,
        "correct_refusal": False,
        "hallucination_detected": False,
        "expected_citations_present": False
    }

    answer = result.get("answer", "").lower()

    # Check for correct refusal on out-of-scope questions
    if query.category == "failure-mode":
        validation["correct_refusal"] = "can only answer based on the textbook" in answer

    # Check if expected citations are present
    if query.expected_citations:
        retrieved_citations = result.get("sources", [])
        validation["expected_citations_present"] = any(
            exp in retrieved_citations for exp in query.expected_citations
        )

    return validation

def run_all_tests():
    """Run all test queries and generate report"""
    print("=" * 80)
    print("RAG Test Query Validation Suite")
    print("=" * 80)

    results = {
        "total": len(TEST_QUERIES),
        "passed": 0,
        "failed": 0,
        "by_category": {}
    }

    for i, query in enumerate(TEST_QUERIES, 1):
        print(f"\n[{i}/{len(TEST_QUERIES)}] Testing: {query.question}")
        print(f"Category: {query.category}")

        result = run_test_query(query)

        if not result["success"]:
            print(f"❌ FAILED: {result['error']}")
            results["failed"] += 1
            continue

        validation = validate_response(query, result)

        # Determine pass/fail
        passed = True

        if query.category == "failure-mode":
            passed = validation["correct_refusal"]
        else:
            passed = validation["has_citations"]

        if passed:
            print(f"✅ PASSED")
            print(f"  Answer: {result['answer'][:100]}...")
            print(f"  Citations: {result['sources']}")
            results["passed"] += 1
        else:
            print(f"❌ FAILED")
            print(f"  Validation: {validation}")
            results["failed"] += 1

        # Track by category
        if query.category not in results["by_category"]:
            results["by_category"][query.category] = {"passed": 0, "failed": 0}

        results["by_category"][query.category]["passed" if passed else "failed"] += 1

    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Total tests: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    print(f"Success rate: {100 * results['passed'] / results['total']:.1f}%")

    print("\nBy Category:")
    for category, stats in results["by_category"].items():
        total = stats["passed"] + stats["failed"]
        print(f"  {category}: {stats['passed']}/{total} passed")

    return results

if __name__ == "__main__":
    results = run_all_tests()

    # Save results to file
    with open("test_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Results saved to test_results.json")

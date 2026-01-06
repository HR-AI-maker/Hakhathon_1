"""
Test script to verify chatbot UI changes
Validates that no backend/debug UI is exposed to users
"""

import re
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def test_frontend_ui():
    """Test that frontend HTML has no backend UI elements"""

    print("=" * 60)
    print("Testing Chatbot UI Fix")
    print("=" * 60)
    print()

    # Read frontend HTML
    with open('frontend/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    tests_passed = 0
    tests_failed = 0

    # Test 1: Check for confidence score display
    print("Test 1: Confidence score should NOT be displayed")
    if 'confidence' not in html_content.lower():
        print("[PASS] No confidence score references found")
        tests_passed += 1
    else:
        print("[FAIL] Confidence score still present in HTML")
        tests_failed += 1
    print()

    # Test 2: Check for execution_time display
    print("Test 2: Execution time should NOT be displayed")
    if 'execution_time' not in html_content.lower():
        print("[PASS] No execution_time references found")
        tests_passed += 1
    else:
        print("[FAIL] Execution time still present in HTML")
        tests_failed += 1
    print()

    # Test 3: Check for model name display
    print("Test 3: Model name should NOT be displayed to users")
    if not re.search(r'model.*gemini|model.*gpt', html_content, re.IGNORECASE):
        print("[PASS] No model name display found")
        tests_passed += 1
    else:
        print("[FAIL] Model name still being displayed")
        tests_failed += 1
    print()

    # Test 4: Verify user-facing elements are present
    print("Test 4: User-facing elements should be present")
    required_elements = [
        ('citation_id', 'Citation ID'),
        ('module', 'Module name'),
        ('section_title', 'Section title')
    ]

    all_present = True
    for element, description in required_elements:
        if element in html_content:
            print(f"  [OK] {description}: Present")
        else:
            print(f"  [X] {description}: Missing")
            all_present = False

    if all_present:
        print("[PASS] All user-facing elements present")
        tests_passed += 1
    else:
        print("[FAIL] Some user-facing elements missing")
        tests_failed += 1
    print()

    # Test 5: Check displayAnswer function structure
    print("Test 5: displayAnswer function should render only user info")

    # Find the displayAnswer function more robustly
    func_start = html_content.find('function displayAnswer(data)')
    if func_start != -1:
        # Find the end by counting braces
        brace_count = 0
        started = False
        func_end = func_start

        for i in range(func_start, len(html_content)):
            if html_content[i] == '{':
                brace_count += 1
                started = True
            elif html_content[i] == '}':
                brace_count -= 1
                if started and brace_count == 0:
                    func_end = i + 1
                    break

        func_code = html_content[func_start:func_end]

        # Should have citation_id, module, section_title
        # Should NOT have confidence, execution_time
        has_user_fields = (
            'citation_id' in func_code and
            'module' in func_code and
            'section_title' in func_code
        )
        has_backend_fields = (
            'confidence' in func_code.lower() or
            'execution_time' in func_code.lower()
        )

        if has_user_fields and not has_backend_fields:
            print("[PASS] displayAnswer renders only user-facing data")
            tests_passed += 1
        else:
            print("[FAIL] displayAnswer has issues")
            if not has_user_fields:
                print("  - Missing user-facing fields")
            if has_backend_fields:
                print("  - Contains backend fields")
            tests_failed += 1
    else:
        print("[FAIL] displayAnswer function not found")
        tests_failed += 1
    print()

    # Test 6: Check CSS cleanup
    print("Test 6: Unused CSS should be removed")
    if '.confidence' not in html_content:
        print("[PASS] .confidence CSS class removed")
        tests_passed += 1
    else:
        print("[FAIL] .confidence CSS class still present")
        tests_failed += 1
    print()

    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Tests Passed: {tests_passed}")
    print(f"Tests Failed: {tests_failed}")
    print(f"Total Tests: {tests_passed + tests_failed}")
    print()

    if tests_failed == 0:
        print("*** ALL TESTS PASSED! ***")
        print("[OK] Frontend UI is clean - no backend debug info exposed")
        return 0
    else:
        print("*** SOME TESTS FAILED ***")
        print("[X] Frontend UI still has issues")
        return 1

if __name__ == '__main__':
    exit_code = test_frontend_ui()
    sys.exit(exit_code)

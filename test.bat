@echo off
REM Test script for Physical AI Textbook RAG Application

echo ========================================
echo Physical AI Textbook - Running Tests
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate

echo [1/3] Testing health endpoint...
curl -s http://localhost:8000/health
echo.
echo.

echo [2/3] Testing sample query...
curl -s -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is Physical AI?\"}"
echo.
echo.

echo [3/3] Running full test suite...
python tests\test_queries.py

echo.
echo ========================================
echo Tests complete!
echo ========================================
pause

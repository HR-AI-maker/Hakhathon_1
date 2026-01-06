@echo off
REM Quick run script for Physical AI Textbook RAG Application
REM This script starts the FastAPI server

echo ========================================
echo Physical AI Textbook - RAG Application
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then: venv\Scripts\activate
    echo Then: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create .env file with your API keys.
    echo See .env.example for template.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Checking environment...
python -c "import fastapi, openai, qdrant_client" 2>nul
if errorlevel 1 (
    echo ERROR: Required packages not installed!
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo Starting RAG API server...
echo Server will run on http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

cd rag_api
python main.py

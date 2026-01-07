"""
Vercel Serverless Function Entry Point
Version: 2.0 - Demo mode with optional dependencies
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rag_api.main import app

# Export the FastAPI app for Vercel
handler = app

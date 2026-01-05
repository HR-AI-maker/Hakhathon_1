"""
Authentication and Session Management
Implements server-side session-based auth for chatbot access control
"""

import os
import secrets
import time
from typing import Optional, Dict
from datetime import datetime, timedelta
from functools import wraps
from fastapi import Request, HTTPException, Response
from fastapi.responses import JSONResponse

# Session configuration
SESSION_LIFETIME = 24 * 60 * 60  # 24 hours in seconds
SESSION_COOKIE_NAME = "session_id"
SECRET_KEY = os.getenv("SESSION_SECRET_KEY", secrets.token_hex(32))

# In-memory session store (use Redis in production)
sessions: Dict[str, dict] = {}


class SessionManager:
    """Manages user sessions with rate limiting"""

    @staticmethod
    def create_session(user_id: str) -> str:
        """Create a new session and return session ID"""
        session_id = secrets.token_urlsafe(32)

        sessions[session_id] = {
            "user_id": user_id,
            "created_at": int(time.time()),
            "last_active": int(time.time()),
            "rate_limit": {
                "requests": 0,
                "window_start": int(time.time())
            }
        }

        return session_id

    @staticmethod
    def get_session(session_id: str) -> Optional[dict]:
        """Get session data if valid, None otherwise"""
        if not session_id or session_id not in sessions:
            return None

        session = sessions[session_id]

        # Check if session expired
        if int(time.time()) - session["created_at"] > SESSION_LIFETIME:
            SessionManager.destroy_session(session_id)
            return None

        # Update last active time
        session["last_active"] = int(time.time())
        return session

    @staticmethod
    def destroy_session(session_id: str) -> bool:
        """Destroy a session"""
        if session_id in sessions:
            del sessions[session_id]
            return True
        return False

    @staticmethod
    def cleanup_expired_sessions():
        """Remove expired sessions (periodic cleanup)"""
        current_time = int(time.time())
        expired = [
            sid for sid, session in sessions.items()
            if current_time - session["created_at"] > SESSION_LIFETIME
        ]
        for sid in expired:
            del sessions[sid]
        return len(expired)


# Hardcoded credentials (MVP - use environment variables in production)
VALID_CREDENTIALS = {
    "demo": "demo123",  # username: password
    "admin": os.getenv("ADMIN_PASSWORD", "admin123")
}


def authenticate_user(username: str, password: str) -> Optional[str]:
    """Validate credentials and return user_id if valid"""
    if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
        return username
    return None


def get_session_from_request(request: Request) -> Optional[dict]:
    """Extract and validate session from request cookies"""
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if not session_id:
        return None
    return SessionManager.get_session(session_id)


def require_auth(func):
    """Decorator to require authentication for endpoint"""
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        session = get_session_from_request(request)

        if not session:
            raise HTTPException(
                status_code=401,
                detail="Authentication required. Please log in."
            )

        # Add session to request state for use in endpoint
        request.state.session = session
        request.state.user_id = session["user_id"]

        return await func(request, *args, **kwargs)

    return wrapper


# Rate limiting constants
RATE_LIMIT_MAX_REQUESTS = 20
RATE_LIMIT_WINDOW = 15 * 60  # 15 minutes in seconds


def check_rate_limit(session: dict) -> tuple[bool, int]:
    """
    Check if request is within rate limit
    Returns: (allowed: bool, retry_after: int)
    """
    current_time = int(time.time())
    rate_limit = session["rate_limit"]

    # Check if we need to reset the window
    if current_time - rate_limit["window_start"] > RATE_LIMIT_WINDOW:
        rate_limit["requests"] = 0
        rate_limit["window_start"] = current_time

    # Check if limit exceeded
    if rate_limit["requests"] >= RATE_LIMIT_MAX_REQUESTS:
        retry_after = RATE_LIMIT_WINDOW - (current_time - rate_limit["window_start"])
        return False, retry_after

    # Increment counter
    rate_limit["requests"] += 1
    return True, 0


def rate_limit(func):
    """Decorator to enforce rate limiting"""
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        session = request.state.session

        allowed, retry_after = check_rate_limit(session)

        if not allowed:
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "Rate limit exceeded",
                    "retry_after": retry_after,
                    "message": f"You can ask again in {retry_after // 60} minutes."
                }
            )

        return await func(request, *args, **kwargs)

    return wrapper

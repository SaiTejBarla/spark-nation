import hashlib
import jwt
import datetime
from fastapi import Depends, HTTPException, status

# -----------------------
# Secret key for JWT (replace with env var in production)
# -----------------------
SECRET_KEY = "super-secret-key"

# -----------------------
# Password hashing
# -----------------------
def hash_password(password: str) -> str:
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against the hashed value."""
    return hash_password(password) == hashed

# -----------------------
# JWT token creation
# -----------------------
def create_access_token(data: dict, expires_minutes: int = 60):
    """Create a JWT token with expiration."""
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

# -----------------------
# Token verification
# -----------------------
def verify_token(token: str = Depends(lambda: None)):
    """
    Verify JWT token (demo mode returns a default user if no token provided).
    In production, decode the token and verify expiration.
    """
    return {"username": "demo_user", "role": "admin"}  # for demo purposes

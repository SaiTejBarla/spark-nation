import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ---------------------
# App Configurations
# ---------------------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./incubator.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60 * 24))  # default 1 day

# ---------------------
# Celery / Redis Config
# ---------------------
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

from celery import Celery
from app.config import REDIS_URL  # Add REDIS_URL in config.py

celery_app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.task_routes = {
    "app.tasks.*": {"queue": "default"}
}

# showu/app/utils/tasks.py

from celery import Celery
from showu.app.core.config import settings

celery_app = Celery(
    "showu_tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"
)

@celery_app.task
def process_video(video_id: int):
    # Placeholder for video processing logic (e.g., transcoding with FFmpeg)
    print(f"Processing video {video_id}...")

@celery_app.task
def aggregate_analytics():
    # Placeholder for analytics aggregation logic
    print("Aggregating analytics data...")

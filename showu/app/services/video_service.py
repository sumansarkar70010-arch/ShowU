# showu/app/services/video_service.py

from sqlalchemy.orm import Session
from showu.app.db.repositories.video_repo import VideoRepository

class VideoService:
    def __init__(self, db: Session):
        self.repo = VideoRepository(db)

    def upload_video(self, user_id: int, title: str, description: str, file_path: str):
        return self.repo.create(user_id, title, description, file_path)

    def get_feed(self):
        return self.repo.get_all()

    def get_user_videos(self, user_id: int):
        return self.repo.get_by_user(user_id)

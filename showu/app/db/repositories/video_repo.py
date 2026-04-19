# showu/app/db/repositories/video_repo.py

from sqlalchemy.orm import Session
from showu.app.db.models.video import Video

class VideoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, title: str, description: str, file_path: str):
        video = Video(user_id=user_id, title=title, description=description, file_path=file_path)
        self.db.add(video)
        self.db.commit()
        self.db.refresh(video)
        return video

    def get_all(self):
        return self.db.query(Video).order_by(Video.created_at.desc()).all()

    def get_by_user(self, user_id: int):
        return self.db.query(Video).filter(Video.user_id == user_id).all()

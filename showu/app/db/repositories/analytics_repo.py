# showu/app/db/repositories/analytics_repo.py

from sqlalchemy.orm import Session
from showu.app.db.models.analytics import Analytics

class AnalyticsRepository:
    def __init__(self, db: Session):
        self.db = db

    def log_action(self, user_id: int, action: str, post_id: int | None = None, video_id: int | None = None):
        entry = Analytics(user_id=user_id, action=action, post_id=post_id, video_id=video_id)
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def get_post_analytics(self, post_id: int):
        return self.db.query(Analytics).filter(Analytics.post_id == post_id).all()

    def get_video_analytics(self, video_id: int):
        return self.db.query(Analytics).filter(Analytics.video_id == video_id).all()

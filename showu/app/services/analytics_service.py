# showu/app/services/analytics_service.py

from sqlalchemy.orm import Session
from showu.app.db.repositories.analytics_repo import AnalyticsRepository

class AnalyticsService:
    def __init__(self, db: Session):
        self.repo = AnalyticsRepository(db)

    def log_action(self, user_id: int, action: str, post_id: int | None = None, video_id: int | None = None):
        return self.repo.log_action(user_id, action, post_id, video_id)

    def get_post_stats(self, post_id: int):
        return self.repo.get_post_analytics(post_id)

    def get_video_stats(self, video_id: int):
        return self.repo.get_video_analytics(video_id)

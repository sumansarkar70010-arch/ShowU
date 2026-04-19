# showu/app/services/story_service.py

from sqlalchemy.orm import Session
from app.db.repositories.story_repo import StoryRepository

class StoryService:
    def __init__(self, db: Session):
        self.repo = StoryRepository(db)

    def create_story(self, user_id: int, media_url: str):
        return self.repo.create(user_id, media_url)

    def get_active_stories(self):
        return self.repo.get_active_stories()

    def get_user_stories(self, user_id: int):
        return self.repo.get_user_stories(user_id)
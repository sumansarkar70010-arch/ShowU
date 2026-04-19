# showu/app/db/repositories/story_repo.py

from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.story import Story

class StoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, media_url: str):
        story = Story(user_id=user_id, media_url=media_url)
        self.db.add(story)
        self.db.commit()
        self.db.refresh(story)
        return story

    def get_active_stories(self):
        return self.db.query(Story).filter(Story.expires_at > datetime.utcnow()).all()

    def get_user_stories(self, user_id: int):
        return self.db.query(Story).filter(
            Story.user_id == user_id, Story.expires_at > datetime.utcnow()
        ).all()
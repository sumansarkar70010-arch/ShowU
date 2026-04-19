# showu/app/api/v1/stories.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from showu.app.db.session import SessionLocal
from showu.app.services.story_service import StoryService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_story(user_id: int, media_url: str, db: Session = Depends(get_db)):
    service = StoryService(db)
    story = service.create_story(user_id, media_url)
    return {"id": story.id, "user_id": story.user_id, "media_url": story.media_url, "expires_at": story.expires_at}

@router.get("/active")
def get_active_stories(db: Session = Depends(get_db)):
    service = StoryService(db)
    stories = service.get_active_stories()
    return [{"id": s.id, "user_id": s.user_id, "media_url": s.media_url, "expires_at": s.expires_at} for s in stories]

@router.get("/user/{user_id}")
def get_user_stories(user_id: int, db: Session = Depends(get_db)):
    service = StoryService(db)
    stories = service.get_user_stories(user_id)
    return [{"id": s.id, "user_id": s.user_id, "media_url": s.media_url, "expires_at": s.expires_at} for s in stories]

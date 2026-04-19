# showu/app/api/v1/posts.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.post_service import PostService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_post(user_id: int, content: str, media_url: str | None = None, db: Session = Depends(get_db)):
    service = PostService(db)
    post = service.create_post(user_id, content, media_url)
    return {"id": post.id, "user_id": post.user_id, "content": post.content, "media_url": post.media_url}

@router.get("/feed")
def get_feed(db: Session = Depends(get_db)):
    service = PostService(db)
    posts = service.get_feed()
    return [{"id": p.id, "user_id": p.user_id, "content": p.content, "media_url": p.media_url} for p in posts]

@router.get("/user/{user_id}")
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    service = PostService(db)
    posts = service.get_user_posts(user_id)
    return [{"id": p.id, "user_id": p.user_id, "content": p.content, "media_url": p.media_url} for p in posts]
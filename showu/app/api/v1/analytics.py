# showu/app/api/v1/analytics.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from showu.app.db.session import SessionLocal
from showu.app.services.analytics_service import AnalyticsService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/log")
def log_action(user_id: int, action: str, post_id: int | None = None, video_id: int | None = None, db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    entry = service.log_action(user_id, action, post_id, video_id)
    return {"id": entry.id, "user_id": entry.user_id, "action": entry.action, "post_id": entry.post_id, "video_id": entry.video_id}

@router.get("/post/{post_id}")
def get_post_stats(post_id: int, db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    stats = service.get_post_stats(post_id)
    return [{"id": s.id, "user_id": s.user_id, "action": s.action, "created_at": s.created_at} for s in stats]

@router.get("/video/{video_id}")
def get_video_stats(video_id: int, db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    stats = service.get_video_stats(video_id)
    return [{"id": s.id, "user_id": s.user_id, "action": s.action, "created_at": s.created_at} for s in stats]

# showu/app/api/v1/videos.py

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
import shutil
from sqlalchemy.orm import Session
from showu.app.db.session import SessionLocal
from showu.app.services.video_service import VideoService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads/videos/"

@router.post("/upload")
def upload_video(user_id: int, title: str, description: str | None = None, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"{UPLOAD_DIR}{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    service = VideoService(db)
    video = service.upload_video(user_id, title, description, file_path)
    return {"id": video.id, "title": video.title, "file_path": video.file_path}

@router.get("/feed")
def get_video_feed(db: Session = Depends(get_db)):
    service = VideoService(db)
    videos = service.get_feed()
    return [{"id": v.id, "title": v.title, "file_path": v.file_path} for v in videos]

@router.get("/user/{user_id}")
def get_user_videos(user_id: int, db: Session = Depends(get_db)):
    service = VideoService(db)
    videos = service.get_user_videos(user_id)
    return [{"id": v.id, "title": v.title, "file_path": v.file_path} for v in videos]

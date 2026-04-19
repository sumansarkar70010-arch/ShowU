# showu/app/db/models/video.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    file_path = Column(String(255), nullable=False)  # local storage path
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="videos")
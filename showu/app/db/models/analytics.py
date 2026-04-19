# showu/app/db/models/analytics.py

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=True)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=True)
    action = Column(String(50), nullable=False)  # e.g. "like", "view", "comment"
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="analytics")
# showu/app/db/models/post.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=True)  # text caption
    media_url = Column(String(255), nullable=True)  # image/video reference
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="posts")
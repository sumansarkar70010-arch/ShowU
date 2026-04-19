# showu/app/db/repositories/post_repo.py

from sqlalchemy.orm import Session
from app.db.models.post import Post

class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, content: str, media_url: str | None = None):
        post = Post(user_id=user_id, content=content, media_url=media_url)
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def get_all(self):
        return self.db.query(Post).order_by(Post.created_at.desc()).all()

    def get_by_user(self, user_id: int):
        return self.db.query(Post).filter(Post.user_id == user_id).all()
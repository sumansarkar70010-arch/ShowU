# showu/app/services/post_service.py

from sqlalchemy.orm import Session
from showu.app.db.repositories.post_repo import PostRepository

class PostService:
    def __init__(self, db: Session):
        self.repo = PostRepository(db)

    def create_post(self, user_id: int, content: str, media_url: str | None = None):
        return self.repo.create(user_id, content, media_url)

    def get_feed(self):
        return self.repo.get_all()

    def get_user_posts(self, user_id: int):
        return self.repo.get_by_user(user_id)

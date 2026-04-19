# showu/app/services/user_service.py

from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db: Session):
        from showu.app.db.repositories.user_repo import UserRepository
        self.repo = UserRepository(db)

    def get_user(self, user_id: int) -> "user | None": # type: ignore
        from showu.app.db.models.user import User
        from showu.app.db.models.user import user
        return self.repo.get_by_id(user_id)

    def update_user(self, user_id: int, username: str | None = None, email: str | None = None):
        from showu.app.db.models.user import User
        user = self.repo.get_by_id(user_id)
        if not user:
            return None
        if username:
            user.username = username
        if email:
            user.email = email
        self.repo.db.commit()
        self.repo.db.refresh(user)
        return user

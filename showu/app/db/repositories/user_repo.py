# showu/app/db/repositories/user_repo.py

from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        from app.db.models.user import User 
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str):
        from app.db.models.user import User 
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str):
        from app.db.models.user import User 
        return self.db.query(User).filter(User.email == email).first()

    def create(self, username: str, email: str, hashed_password: str):
        from app.db.models.user import User 
        user = User(username=username, email=email, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
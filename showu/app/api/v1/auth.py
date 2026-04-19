# showu/app/api/v1/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from showu.app.db.session import SessionLocal
from showu.app.db.repositories.user_repo import UserRepository
from showu.app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if repo.get_by_email(email):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = auth_service.hash_password(password)
    user = repo.create(username, email, hashed_pw)
    return {"id": user.id, "username": user.username, "email": user.email}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_by_email(email)
    if not user or not auth_service.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth_service.create_access_token(subject=user.email)
    return {"access_token": token, "token_type": "bearer"}

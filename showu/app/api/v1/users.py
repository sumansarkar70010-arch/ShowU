# showu/app/api/v1/users.py

from showu.app.services.user_service import UserService 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from showu.app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "email": user.email}

@router.put("/{user_id}")
def update_user(user_id: int, username: str | None = None, email: str | None = None, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.update_user(user_id, username, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "email": user.email}

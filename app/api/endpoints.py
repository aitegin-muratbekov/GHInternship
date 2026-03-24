from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_service import UserService  

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()


@router.get("/hello")

def say_hello():
    return {"message": "Hello World"}

@router.post("/users")

def register_user(username: str, password:str, db : Session = Depends(get_db)):
    service = UserService(db)

    user = service.register_user(username, password)

    if not user:
        return {"error": "User already exists"}
        
    return {"id": user.id, "username": user.username}

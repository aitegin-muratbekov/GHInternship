from sqlalchemy.orm import Session
from app.repository.user_repo import UserRepository
from app.core.security import PasswordHelper

# Название должно быть в точности UserService
class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, username: str, password: str):
        existing_user = self.repository.get_by_username(username)
        if existing_user:
            return None
        
        # Имитация хеширования (позже заменим на реальное)
        password_hash = PasswordHelper.hash_password(password)
        
        return self.repository.create(username, password_hash)
        
    
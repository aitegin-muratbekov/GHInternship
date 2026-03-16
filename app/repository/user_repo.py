from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    # Аналог userRepository.findById(id)
    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    # Аналог userRepository.findByUsername(name)
    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    # Аналог userRepository.save(user)
    def create(self, username: str, password_hash: str):
        db_user = User(username=username, password_hash=password_hash)
        self.db.add(db_user)
        self.db.commit() # В Spring это делает @Transactional
        self.db.refresh(db_user)
        return db_user
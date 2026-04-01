from sqlalchemy.orm import Session
from app.models.user import User
from app.repository.user_repo import UserRepository
from app.core.security import PasswordHelper
from app.schemas.user_schemas import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, user_data: UserCreate):
        """
        Аналог registerUser(UserRegistrationDto userData)
        """
        # 1. Проверяем, занято ли имя (Challenge: Handling existing username)
        existing_user = self.repository.get_by_username(user_data.username)
        if existing_user:
            # В будущем тут можно выбрасывать кастомное исключение
            return None 
        
        # 2. Хешируем пароль (Challenge: Plain-text to hash)
        hashed_password = PasswordHelper.hash_password(user_data.password)
        
        # 3. Сохраняем через репозиторий
        return self.repository.create(
            username=user_data.username, 
            password_hash=hashed_password
        )

    def find_by_username(self, username: str):
        """
        Аналог findByUsername(String username)
        """
        return self.repository.get_by_username(username)

    def verify_user(self, username: str, password: str):
        """
        Логика для будущего эндпоинта /login
        """
        user = self.find_by_username(username)
        if not user:
            return None
            
        # Используем matches() аналог — verify_password
        if PasswordHelper.verify_password(password, user.password_hash):
            return user
        return None
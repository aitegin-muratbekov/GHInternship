import pytest
from unittest.mock import MagicMock
from app.services.user_service import UserService
from app.schemas.user_schemas import UserCreate

def test_register_user_success():
    # 1. Создаем мок репозитория
    mock_repo = MagicMock()
    
    # Настраиваем: сначала ищем юзера — его НЕТ (None)
    mock_repo.get_user_by_username.return_value = None
    
    # Настраиваем: создание юзера возвращает объект
    mock_user = MagicMock(id=1, username="test_user")
    mock_repo.create_user.return_value = mock_user

    # 2. Создаем сервис и ОБЯЗАТЕЛЬНО передаем экземпляр мока db
    service = UserService(db=MagicMock()) # Добавили скобки тут
    service.repository = mock_repo

    # 3. Запускаем
    user_data = UserCreate(username="test_user", password="password000")
    result = service.register_user(user_data)

    # 4. Проверяем
    assert result is not None, "Service returned None, check your mock setup"
    assert result.username == "test_user"
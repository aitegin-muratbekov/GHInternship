import bcrypt

class PasswordHelper:
    @staticmethod
    def hash_password(password: str) -> str:
        # Превращаем строку в байты, генерируем соль и хешируем
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pwd_bytes, salt)
        return hashed.decode('utf-8') # Возвращаем строку для базы

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        # Проверяем совпадение
        return bcrypt.checkpw(
            plain_password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        )
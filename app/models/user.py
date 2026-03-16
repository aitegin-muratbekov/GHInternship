from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users" # Как таблица будет называться в БД

    # Каждое поле — это колонка в таблице
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String, unique=True, index=True)
    password_hash = Column(String) 
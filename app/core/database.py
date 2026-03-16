from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 2. Создаем "двигатель". 
# connect_args нужны только для SQLite, чтобы она не ругалась на разные потоки.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Создаем "заготовку" для сессий. 
# Каждый раз, когда нам нужно что-то взять из БД, мы будем звать SessionLocal()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Базовый класс. От него мы будем "наследовать" наши таблицы.
# Это связующее звено между кодом и реальными таблицами в БД.
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
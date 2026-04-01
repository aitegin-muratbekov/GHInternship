# Project_1: FastAPI Foundation (Week 2)

## 🚀 Стек технологий
- **Python 3.12+**
- **FastAPI** — веб-фреймворк (аналог Spring Web).
- **Uvicorn** — сервер приложений (аналог встроенного Tomcat).
- **SQLAlchemy** — ORM для работы с данными (аналог Spring Data JPA).
- **SQLite** — база данных для разработки (аналог H2).
- **Pydantic** — валидация данных (аналог Lombok + DTO).

2. Настройка виртуального окружения

Bash
python -m venv .venv
# Для macOS/Linux:
source .venv/bin/activate
# Для Windows:
.venv\Scripts\activate
3. Установка зависимостей

Bash
pip install -r requirements.txt
4. Запуск сервера

Bash
uvicorn main:app --reload

### 1. Клонирование репозитория
```bash
git clone [https://github.com/твой-логин/Project_1.git](https://github.com/твой-логин/Project_1.git)
cd Project_1
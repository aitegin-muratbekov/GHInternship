from fastapi import FastAPI, Depends
from app.api.endpoints import router as router
from app.core.database import engine, Base
from app.models.user import User

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer



# Это команда "создать таблицы, если их нет" (аналог ddl-auto=update)
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router)
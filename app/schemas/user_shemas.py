from pydantic import BaseModel, Field

# Это твой UserRegistrationDto
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=4)

# Это то, что мы будем возвращать клиенту (без пароля!)
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True # Позволяет Pydantic работать с моделями SQLAlchemy
from typing import Optional
from pydantic import BaseModel, EmailStr
from app.db.models.usuario import UserRole

# Propiedades compartidas
class UserBase(BaseModel):
    usuario: Optional[str] = None
    rol: Optional[UserRole] = None
    empresa_id: Optional[int] = None

# Propiedades para creación (Signup/Admin)
class UserCreate(UserBase):
    usuario: str
    password: str
    rol: UserRole

# Propiedades para actualizar
class UserUpdate(UserBase):
    password: Optional[str] = None

# Propiedades para retornar vía API
class User(UserBase):
    id: int

    class Config:
        from_attributes = True

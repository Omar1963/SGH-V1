from typing import Optional
from pydantic import BaseModel

class PersonaBase(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    cuil: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    empresa_id: Optional[int] = None

class PersonaCreate(PersonaBase):
    nombre: str
    apellido: str
    cuil: str
    empresa_id: int

class PersonaUpdate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int

    class Config:
        from_attributes = True

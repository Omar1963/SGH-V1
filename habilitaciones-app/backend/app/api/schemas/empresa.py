from typing import Optional
from pydantic import BaseModel

class EmpresaBase(BaseModel):
    razon_social: Optional[str] = None
    cuit: Optional[str] = None
    domicilio_legal: Optional[str] = None
    jurisdiccion: Optional[str] = None

class EmpresaCreate(EmpresaBase):
    razon_social: str
    cuit: str

class EmpresaUpdate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class Config:
        from_attributes = True

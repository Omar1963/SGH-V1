from datetime import date
from typing import Optional

from pydantic import BaseModel


class EstadoBase(BaseModel):
    persona_id: Optional[int] = None
    tipo: Optional[str] = None
    jurisdiccion: Optional[str] = None
    valor: Optional[str] = None
    fecha: Optional[date] = None


class EstadoCreate(EstadoBase):
    persona_id: int
    tipo: str
    jurisdiccion: str
    valor: str
    fecha: date


class EstadoUpdate(BaseModel):
    tipo: Optional[str] = None
    jurisdiccion: Optional[str] = None
    valor: Optional[str] = None
    fecha: Optional[date] = None


class Estado(EstadoBase):
    id: int

    class Config:
        from_attributes = True

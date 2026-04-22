from typing import Optional
from pydantic import BaseModel
from datetime import date

class HabilitacionBase(BaseModel):
    persona_id: Optional[int] = None
    jurisdiccion: Optional[str] = None
    numero_credencial: Optional[str] = None
    fecha_desde: Optional[date] = None
    fecha_hasta: Optional[date] = None
    estado: Optional[str] = None

class HabilitacionCreate(HabilitacionBase):
    persona_id: int
    jurisdiccion: str
    numero_credencial: str
    fecha_desde: date
    fecha_hasta: date
    estado: str

class HabilitacionUpdate(HabilitacionBase):
    pass

class Habilitacion(HabilitacionBase):
    id: int

    class Config:
        from_attributes = True

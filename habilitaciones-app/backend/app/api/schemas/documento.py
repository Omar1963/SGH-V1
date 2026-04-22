from typing import Optional
from pydantic import BaseModel
from datetime import date
from app.db.models.documento import EstadoDocumento

class DocumentoBase(BaseModel):
    persona_id: Optional[int] = None
    tipo: Optional[str] = None
    jurisdiccion: Optional[str] = None
    fecha_presentacion: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    estado: Optional[EstadoDocumento] = None

class DocumentoCreate(DocumentoBase):
    persona_id: int
    tipo: str
    jurisdiccion: str
    fecha_presentacion: date

class DocumentoUpdate(BaseModel):
    tipo: Optional[str] = None
    jurisdiccion: Optional[str] = None
    fecha_presentacion: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    estado: Optional[EstadoDocumento] = None

class Documento(DocumentoBase):
    id: int
    path_archivo: Optional[str] = None

    class Config:
        from_attributes = True

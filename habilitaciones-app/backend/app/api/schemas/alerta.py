from typing import Optional
from pydantic import BaseModel
from datetime import date

class AlertaBase(BaseModel):
    persona_id: Optional[int] = None
    tipo: Optional[str] = None
    fecha: Optional[date] = None
    mensaje: Optional[str] = None
    estado: Optional[str] = None

class AlertaCreate(AlertaBase):
    persona_id: int
    tipo: str
    fecha: date
    mensaje: str

class Alerta(AlertaBase):
    id: int

    class Config:
        from_attributes = True

# Esquema para el Dashboard
class DashboardSummary(BaseModel):
    habilitaciones_vigentes: int
    habilitaciones_por_vencer: int
    habilitaciones_vencidas: int
    alertas_activas: int
    documentos_pendientes_revision: int

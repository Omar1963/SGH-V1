from typing import Any, List, Optional
from pydantic import BaseModel, Field

class DashboardWidgetBase(BaseModel):
    tipo: str
    dataset_key: str
    metric: str
    dimension: Optional[str] = None
    agregacion: Optional[str] = None
    orden: Optional[int] = Field(default=0)
    config: Optional[dict[str, Any]] = Field(default_factory=dict)

class DashboardWidgetCreate(DashboardWidgetBase):
    pass

class DashboardWidgetUpdate(BaseModel):
    tipo: Optional[str] = None
    dataset_key: Optional[str] = None
    metric: Optional[str] = None
    dimension: Optional[str] = None
    agregacion: Optional[str] = None
    orden: Optional[int] = None
    config: Optional[dict[str, Any]] = None

class DashboardFilterBase(BaseModel):
    campo: str
    operador: str
    valor: Optional[Any] = None
    scope: Optional[str] = "dashboard"
    widget_id: Optional[int] = None

class DashboardShareCreate(BaseModel):
    target_user_id: Optional[int] = None
    target_role: Optional[str] = None
    target_empresa_id: Optional[int] = None
    permisos: Optional[dict[str, Any]] = Field(default_factory=dict)

class DashboardCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    visibilidad: Optional[str] = "PRIVATE"
    widgets: Optional[List[DashboardWidgetCreate]] = Field(default_factory=list)
    filters: Optional[List[DashboardFilterBase]] = Field(default_factory=list)

class DashboardUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    visibilidad: Optional[str] = None

class DashboardWidget(DashboardWidgetBase):
    id: int

    class Config:
        from_attributes = True

class DashboardFilter(DashboardFilterBase):
    id: int

    class Config:
        from_attributes = True

class DashboardShare(DashboardShareCreate):
    id: int

    class Config:
        from_attributes = True

class DashboardDetail(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    visibilidad: str
    owner_id: int
    empresa_id: Optional[int] = None
    widgets: List[DashboardWidget] = Field(default_factory=list)
    filters: List[DashboardFilter] = Field(default_factory=list)
    shares: List[DashboardShare] = Field(default_factory=list)

    class Config:
        from_attributes = True

class DashboardCatalog(BaseModel):
    datasets: List[str]
    metrics: List[str]
    dimensions: List[str]
    chart_types: List[str]

class DashboardQueryResult(BaseModel):
    dashboard_id: int
    results: List[dict[str, Any]]
    message: Optional[str] = None

class DashboardSummary(BaseModel):
    habilitaciones_vigentes: int
    habilitaciones_por_vencer: int
    habilitaciones_vencidas: int
    alertas_activas: int
    documentos_pendientes_revision: int

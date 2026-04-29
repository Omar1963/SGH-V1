from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.api.dependencies.auth import get_current_user
from app.api.schemas.dashboard import (
    DashboardCatalog,
    DashboardCreate,
    DashboardDetail,
    DashboardQueryResult,
    DashboardShare,
    DashboardShareCreate,
    DashboardSummary,
    DashboardUpdate,
    DashboardWidget,
    DashboardWidgetCreate,
    DashboardWidgetUpdate,
)
from app.domain.dashboard.service import DashboardService
from app.domain.personas.repository import PersonaRepository
from app.domain.alertas.service import AlertaService

router = APIRouter()

async def get_alerta_service(db: AsyncSession = Depends(get_db)) -> AlertaService:
    persona_repo = PersonaRepository(db)
    return AlertaService(db, persona_repo)

async def get_dashboard_service(db: AsyncSession = Depends(get_db)) -> DashboardService:
    return DashboardService(db)

@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary(
    current_user: Usuario = Depends(get_current_user),
    service: AlertaService = Depends(get_alerta_service)
):
    """
    Retorna el resumen consolidado de estados, alertas y documentos.
    Si el usuario es EMPRESA, los datos están filtrados por su empresa_id.
    """
    return await service.get_dashboard_summary(current_user)

@router.get("/catalog", response_model=DashboardCatalog)
async def get_dashboard_catalog(
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    return await service.get_dashboard_catalog()

@router.get("/builder", response_model=list[DashboardDetail])
async def list_dashboards(
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    return await service.get_dashboards(current_user)

@router.post("/builder", response_model=DashboardDetail, status_code=status.HTTP_201_CREATED)
async def create_dashboard(
    payload: DashboardCreate,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    return await service.create_dashboard(current_user, payload)

@router.get("/builder/{dashboard_id}", response_model=DashboardDetail)
async def get_dashboard(
    dashboard_id: int,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    return dashboard

@router.patch("/builder/{dashboard_id}", response_model=DashboardDetail)
async def update_dashboard(
    dashboard_id: int,
    payload: DashboardUpdate,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    return await service.update_dashboard(dashboard_id, payload)

@router.post("/builder/{dashboard_id}/widgets", response_model=DashboardWidget, status_code=status.HTTP_201_CREATED)
async def add_widget(
    dashboard_id: int,
    payload: DashboardWidgetCreate,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    return await service.add_widget(dashboard_id, payload)

@router.patch("/builder/{dashboard_id}/widgets/{widget_id}", response_model=DashboardWidget)
async def update_widget(
    dashboard_id: int,
    widget_id: int,
    payload: DashboardWidgetUpdate,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    widget = await service.update_widget(widget_id, payload)
    if not widget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Widget no encontrado.")
    return widget

@router.delete("/builder/{dashboard_id}/widgets/{widget_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_widget(
    dashboard_id: int,
    widget_id: int,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    await service.delete_widget(widget_id)
    return None

@router.post("/builder/{dashboard_id}/query", response_model=DashboardQueryResult)
async def query_dashboard(
    dashboard_id: int,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    return await service.query_dashboard(dashboard_id)

@router.post("/builder/{dashboard_id}/share", response_model=DashboardShare, status_code=status.HTTP_201_CREATED)
async def share_dashboard(
    dashboard_id: int,
    payload: DashboardShareCreate,
    current_user: Usuario = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
):
    dashboard = await service.get_dashboard(current_user, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dashboard no encontrado o acceso denegado.")
    return await service.share_dashboard(dashboard_id, payload)

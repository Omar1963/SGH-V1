from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.api.dependencies.auth import get_current_user, RoleChecker
from app.api.schemas.alerta import DashboardSummary
from app.domain.alertas.service import AlertaService
from app.domain.personas.repository import PersonaRepository

router = APIRouter()

async def get_alerta_service(db: AsyncSession = Depends(get_db)) -> AlertaService:
    persona_repo = PersonaRepository(db)
    return AlertaService(db, persona_repo)

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

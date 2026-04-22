from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.api.dependencies.auth import get_current_user, RoleChecker
from app.api.schemas.habilitacion import Habilitacion, HabilitacionCreate
from app.domain.habilitaciones.repository import HabilitacionRepository
from app.domain.habilitaciones.service import HabilitacionService
from app.domain.personas.repository import PersonaRepository

router = APIRouter()

# Roles permitidos
allowed_roles = [
    UserRole.ADMIN_CONSULTORA, 
    UserRole.RESPONSABLE_HABILITACIONES, 
    UserRole.OPERADOR_CONSULTORA,
    UserRole.EMPRESA
]
access_required = RoleChecker(allowed_roles)

async def get_habilitacion_service(db: AsyncSession = Depends(get_db)) -> HabilitacionService:
    repo = HabilitacionRepository(db)
    persona_repo = PersonaRepository(db)
    return HabilitacionService(repo, persona_repo)

@router.get("/", response_model=List[Habilitacion])
async def list_habilitaciones(
    current_user: Usuario = Depends(access_required),
    service: HabilitacionService = Depends(get_habilitacion_service)
):
    return await service.list_habilitaciones(current_user)

@router.post("/", response_model=Habilitacion, status_code=status.HTTP_201_CREATED)
async def create_habilitacion(
    hab_in: HabilitacionCreate,
    current_user: Usuario = Depends(access_required),
    service: HabilitacionService = Depends(get_habilitacion_service)
):
    return await service.create_habilitacion(hab_in, current_user)

@router.get("/{hab_id}", response_model=Habilitacion)
async def get_habilitacion(
    hab_id: int,
    current_user: Usuario = Depends(access_required),
    service: HabilitacionService = Depends(get_habilitacion_service)
):
    return await service.get_habilitacion_secured(hab_id, current_user)

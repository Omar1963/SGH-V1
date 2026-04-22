from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.api.dependencies.auth import get_current_user, RoleChecker
from app.api.schemas.persona import Persona, PersonaCreate, PersonaUpdate
from app.domain.personas.repository import PersonaRepository
from app.domain.personas.service import PersonaService

router = APIRouter()

# Roles que pueden acceder a personas
allowed_roles = [
    UserRole.ADMIN_CONSULTORA, 
    UserRole.RESPONSABLE_HABILITACIONES, 
    UserRole.OPERADOR_CONSULTORA,
    UserRole.EMPRESA
]
access_required = RoleChecker(allowed_roles)

async def get_persona_service(db: AsyncSession = Depends(get_db)) -> PersonaService:
    repo = PersonaRepository(db)
    return PersonaService(repo)

@router.get("/", response_model=List[Persona])
async def list_personas(
    current_user: Usuario = Depends(access_required),
    service: PersonaService = Depends(get_persona_service)
):
    return await service.list_personas(current_user)

@router.post("/", response_model=Persona, status_code=status.HTTP_201_CREATED)
async def create_persona(
    persona_in: PersonaCreate,
    current_user: Usuario = Depends(access_required),
    service: PersonaService = Depends(get_persona_service)
):
    return await service.create_persona(persona_in, current_user)

@router.get("/{persona_id}", response_model=Persona)
async def get_persona(
    persona_id: int,
    current_user: Usuario = Depends(access_required),
    service: PersonaService = Depends(get_persona_service)
):
    return await service.get_persona_secured(persona_id, current_user)

@router.put("/{persona_id}", response_model=Persona)
async def update_persona(
    persona_id: int,
    persona_in: PersonaUpdate,
    current_user: Usuario = Depends(access_required),
    service: PersonaService = Depends(get_persona_service)
):
    return await service.update_persona(persona_id, persona_in, current_user)

@router.delete("/{persona_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_persona(
    persona_id: int,
    current_user: Usuario = Depends(access_required),
    service: PersonaService = Depends(get_persona_service)
):
    await service.delete_persona(persona_id, current_user)
    return None

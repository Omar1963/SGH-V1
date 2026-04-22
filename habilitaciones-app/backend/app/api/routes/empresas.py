from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.db.models.usuario import UserRole
from app.api.dependencies.auth import RoleChecker
from app.api.schemas.empresa import Empresa, EmpresaCreate, EmpresaUpdate
from app.domain.empresas.repository import EmpresaRepository
from app.domain.empresas.service import EmpresaService

router = APIRouter()

# Solo administradores pueden gestionar empresas
admin_required = RoleChecker([UserRole.ADMIN_CONSULTORA, UserRole.RESPONSABLE_HABILITACIONES])

async def get_empresa_service(db: AsyncSession = Depends(get_db)) -> EmpresaService:
    repo = EmpresaRepository(db)
    return EmpresaService(repo)

@router.get("/", response_model=List[Empresa], dependencies=[Depends(admin_required)])
async def list_empresas(service: EmpresaService = Depends(get_empresa_service)):
    return await service.list_empresas()

@router.post("/", response_model=Empresa, status_code=status.HTTP_201_CREATED, dependencies=[Depends(admin_required)])
async def create_empresa(empresa_in: EmpresaCreate, service: EmpresaService = Depends(get_empresa_service)):
    return await service.create_empresa(empresa_in)

@router.get("/{empresa_id}", response_model=Empresa, dependencies=[Depends(admin_required)])
async def get_empresa(empresa_id: int, service: EmpresaService = Depends(get_empresa_service)):
    return await service.get_empresa(empresa_id)

@router.put("/{empresa_id}", response_model=Empresa, dependencies=[Depends(admin_required)])
async def update_empresa(
    empresa_id: int, 
    empresa_in: EmpresaUpdate, 
    service: EmpresaService = Depends(get_empresa_service)
):
    return await service.update_empresa(empresa_id, empresa_in)

@router.delete("/{empresa_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(admin_required)])
async def delete_empresa(empresa_id: int, service: EmpresaService = Depends(get_empresa_service)):
    await service.delete_empresa(empresa_id)
    return None

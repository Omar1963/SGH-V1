from typing import List, Optional
from fastapi import HTTPException, status
from app.domain.empresas.repository import EmpresaRepository
from app.api.schemas.empresa import EmpresaCreate, EmpresaUpdate
from app.db.models.empresa import Empresa

class EmpresaService:
    def __init__(self, repository: EmpresaRepository):
        self.repository = repository

    async def list_empresas(self) -> List[Empresa]:
        return await self.repository.get_all()

    async def get_empresa(self, empresa_id: int) -> Empresa:
        empresa = await self.repository.get_by_id(empresa_id)
        if not empresa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Empresa con ID {empresa_id} no encontrada"
            )
        return empresa

    async def create_empresa(self, empresa_in: EmpresaCreate) -> Empresa:
        # Validar CUIT duplicado
        existing = await self.repository.get_by_cuit(empresa_in.cuit)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El CUIT ya se encuentra registrado"
            )
        return await self.repository.create(empresa_in.model_dump())

    async def update_empresa(self, empresa_id: int, empresa_in: EmpresaUpdate) -> Empresa:
        await self.get_empresa(empresa_id) # Verificar existencia
        updated = await self.repository.update(empresa_id, empresa_in.model_dump(exclude_unset=True))
        return updated

    async def delete_empresa(self, empresa_id: int) -> bool:
        await self.get_empresa(empresa_id)
        return await self.repository.delete(empresa_id)

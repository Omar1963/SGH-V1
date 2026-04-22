from typing import List, Optional
from fastapi import HTTPException, status
from app.domain.personas.repository import PersonaRepository
from app.api.schemas.persona import PersonaCreate, PersonaUpdate
from app.db.models.persona import Persona
from app.db.models.usuario import Usuario, UserRole

class PersonaService:
    def __init__(self, repository: PersonaRepository):
        self.repository = repository

    async def list_personas(self, current_user: Usuario) -> List[Persona]:
        # Multi-tenancy: Si es rol EMPRESA, solo ve los suyos
        empresa_id = None
        if current_user.rol == UserRole.EMPRESA:
            empresa_id = current_user.empresa_id
        
        return await self.repository.get_all(empresa_id=empresa_id)

    async def get_persona_secured(self, persona_id: int, current_user: Usuario) -> Persona:
        persona = await self.repository.get_by_id(persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona no encontrada")
        
        # Validar pertenencia si es rol EMPRESA
        if current_user.rol == UserRole.EMPRESA and persona.empresa_id != current_user.empresa_id:
            raise HTTPException(status_code=403, detail="No tiene permisos para acceder a esta persona")
        
        return persona

    async def create_persona(self, persona_in: PersonaCreate, current_user: Usuario) -> Persona:
        # Validar CUIL duplicado
        existing = await self.repository.get_by_cuil(persona_in.cuil)
        if existing:
            raise HTTPException(status_code=400, detail="El CUIL ya está registrado")
        
        # Si es rol EMPRESA, forzar su propio empresa_id
        data = persona_in.model_dump()
        if current_user.rol == UserRole.EMPRESA:
            data["empresa_id"] = current_user.empresa_id
            
        return await self.repository.create(data)

    async def update_persona(self, persona_id: int, persona_in: PersonaUpdate, current_user: Usuario) -> Persona:
        await self.get_persona_secured(persona_id, current_user)
        updated = await self.repository.update(persona_id, persona_in.model_dump(exclude_unset=True))
        return updated

    async def delete_persona(self, persona_id: int, current_user: Usuario) -> bool:
        await self.get_persona_secured(persona_id, current_user)
        return await self.repository.delete(persona_id)

from typing import List, Optional
from fastapi import HTTPException, status
from app.db.models.otros import Habilitacion
from app.db.models.usuario import Usuario, UserRole
from app.domain.habilitaciones.repository import HabilitacionRepository
from app.domain.personas.repository import PersonaRepository
from app.api.schemas.habilitacion import HabilitacionCreate

class HabilitacionService:
    def __init__(self, repository: HabilitacionRepository, persona_repo: PersonaRepository):
        self.repository = repository
        self.persona_repo = persona_repo

    async def list_habilitaciones(self, current_user: Usuario) -> List[Habilitacion]:
        persona_ids = None
        if current_user.rol == UserRole.EMPRESA:
            personas = await self.persona_repo.get_all(empresa_id=current_user.empresa_id)
            persona_ids = [p.id for p in personas]
            if not persona_ids:
                return []
        
        return await self.repository.get_all(persona_ids=persona_ids)

    async def create_habilitacion(self, hab_in: HabilitacionCreate, current_user: Usuario) -> Habilitacion:
        # Validar permisos sobre la persona
        persona = await self.persona_repo.get_by_id(hab_in.persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona no encontrada")
        
        if current_user.rol == UserRole.EMPRESA and persona.empresa_id != current_user.empresa_id:
            raise HTTPException(status_code=403, detail="No tiene permisos para esta persona")

        return await self.repository.create(hab_in.model_dump())

    async def get_habilitacion_secured(self, hab_id: int, current_user: Usuario) -> Habilitacion:
        hab = await self.repository.get_by_id(hab_id)
        if not hab:
            raise HTTPException(status_code=404, detail="Habilitación no encontrada")
        
        if current_user.rol == UserRole.EMPRESA:
            if hab.persona.empresa_id != current_user.empresa_id:
                raise HTTPException(status_code=403, detail="Acceso denegado")
        
        return hab

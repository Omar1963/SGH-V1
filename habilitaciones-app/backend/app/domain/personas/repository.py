from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.db.models.persona import Persona

class PersonaRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, empresa_id: Optional[int] = None) -> List[Persona]:
        query = select(Persona)
        if empresa_id:
            query = query.where(Persona.empresa_id == empresa_id)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, persona_id: int) -> Optional[Persona]:
        result = await self.db.execute(select(Persona).where(Persona.id == persona_id))
        return result.scalar_one_or_none()

    async def get_by_cuil(self, cuil: str) -> Optional[Persona]:
        result = await self.db.execute(select(Persona).where(Persona.cuil == cuil))
        return result.scalar_one_or_none()

    async def create(self, persona_data: dict) -> Persona:
        db_persona = Persona(**persona_data)
        self.db.add(db_persona)
        await self.db.commit()
        await self.db.refresh(db_persona)
        return db_persona

    async def update(self, persona_id: int, persona_data: dict) -> Optional[Persona]:
        query = (
            update(Persona)
            .where(Persona.id == persona_id)
            .values(**persona_data)
            .returning(Persona)
        )
        result = await self.db.execute(query)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete(self, persona_id: int) -> bool:
        query = delete(Persona).where(Persona.id == persona_id)
        await self.db.execute(query)
        await self.db.commit()
        return True

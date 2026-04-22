from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func
from app.db.models.otros import Habilitacion

class HabilitacionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, persona_ids: Optional[List[int]] = None) -> List[Habilitacion]:
        query = select(Habilitacion)
        if persona_ids is not None:
            query = query.where(Habilitacion.persona_id.in_(persona_ids))
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, hab_id: int) -> Optional[Habilitacion]:
        result = await self.db.execute(select(Habilitacion).where(Habilitacion.id == hab_id))
        return result.scalar_one_or_none()

    async def create(self, hab_data: dict) -> Habilitacion:
        db_hab = Habilitacion(**hab_data)
        self.db.add(db_hab)
        await self.db.commit()
        await self.db.refresh(db_hab)
        return db_hab

    # Metodos especificos para Dashboard
    async def count_by_status(self, persona_ids: Optional[List[int]], status: str) -> int:
        query = select(func.count(Habilitacion.id)).where(Habilitacion.estado == status)
        if persona_ids is not None:
            query = query.where(Habilitacion.persona_id.in_(persona_ids))
        result = await self.db.execute(query)
        return result.scalar() or 0

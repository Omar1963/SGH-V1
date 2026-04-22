from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.db.models.empresa import Empresa

class EmpresaRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Empresa]:
        result = await self.db.execute(select(Empresa))
        return result.scalars().all()

    async def get_by_id(self, empresa_id: int) -> Optional[Empresa]:
        result = await self.db.execute(select(Empresa).where(Empresa.id == empresa_id))
        return result.scalar_one_or_none()

    async def get_by_cuit(self, cuit: str) -> Optional[Empresa]:
        result = await self.db.execute(select(Empresa).where(Empresa.cuit == cuit))
        return result.scalar_one_or_none()

    async def create(self, empresa_data: dict) -> Empresa:
        db_empresa = Empresa(**empresa_data)
        self.db.add(db_empresa)
        await self.db.commit()
        await self.db.refresh(db_empresa)
        return db_empresa

    async def update(self, empresa_id: int, empresa_data: dict) -> Optional[Empresa]:
        query = (
            update(Empresa)
            .where(Empresa.id == empresa_id)
            .values(**empresa_data)
            .returning(Empresa)
        )
        result = await self.db.execute(query)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete(self, empresa_id: int) -> bool:
        query = delete(Empresa).where(Empresa.id == empresa_id)
        await self.db.execute(query)
        await self.db.commit()
        return True

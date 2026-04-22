from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.db.models.documento import Documento, EstadoDocumento

class DocumentoRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, persona_ids: Optional[List[int]] = None) -> List[Documento]:
        query = select(Documento)
        if persona_ids is not None:
            query = query.where(Documento.persona_id.in_(persona_ids))
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, doc_id: int) -> Optional[Documento]:
        result = await self.db.execute(select(Documento).where(Documento.id == doc_id))
        return result.scalar_one_or_none()

    async def create(self, doc_data: dict) -> Documento:
        db_doc = Documento(**doc_data)
        self.db.add(db_doc)
        await self.db.commit()
        await self.db.refresh(db_doc)
        return db_doc

    async def update(self, doc_id: int, doc_data: dict) -> Optional[Documento]:
        query = (
            update(Documento)
            .where(Documento.id == doc_id)
            .values(**doc_data)
            .returning(Documento)
        )
        result = await self.db.execute(query)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete(self, doc_id: int) -> bool:
        query = delete(Documento).where(Documento.id == doc_id)
        await self.db.execute(query)
        await self.db.commit()
        return True

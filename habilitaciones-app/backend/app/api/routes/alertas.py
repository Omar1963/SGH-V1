from datetime import date
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import get_current_user
from app.api.schemas.alerta import Alerta, AlertaCreate
from app.db.models.otros import Alerta as AlertaModel
from app.db.models.usuario import Usuario, UserRole
from app.db.session import get_db
from app.domain.personas.repository import PersonaRepository

router = APIRouter()


@router.get("/", response_model=List[Alerta])
async def list_alertas(
    current_user: Usuario = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(AlertaModel)
    if current_user.rol == UserRole.EMPRESA:
        persona_repo = PersonaRepository(db)
        personas = await persona_repo.get_all(empresa_id=current_user.empresa_id)
        persona_ids = [p.id for p in personas]
        if not persona_ids:
            return []
        query = query.where(AlertaModel.persona_id.in_(persona_ids))
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/", response_model=Alerta, status_code=status.HTTP_201_CREATED)
async def create_alerta(
    payload: AlertaCreate,
    current_user: Usuario = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Empresas no pueden crear alertas globales/manuales
    if current_user.rol == UserRole.EMPRESA:
        from fastapi import HTTPException

        raise HTTPException(status_code=403, detail="Accion no permitida")

    alerta = AlertaModel(
        persona_id=payload.persona_id,
        tipo=payload.tipo,
        fecha=payload.fecha,
        mensaje=payload.mensaje,
        estado="ACTIVA",
    )
    db.add(alerta)
    await db.commit()
    await db.refresh(alerta)
    return alerta


@router.post("/emitir")
async def emitir_alertas(
    current_user: Usuario = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Placeholder operativo: en esta etapa deja trazabilidad de ejecucion.
    if current_user.rol == UserRole.EMPRESA:
        from fastapi import HTTPException

        raise HTTPException(status_code=403, detail="Accion no permitida")

    return {"message": "Proceso de emision ejecutado", "fecha": date.today().isoformat()}

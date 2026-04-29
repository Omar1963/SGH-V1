from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import RoleChecker
from app.api.schemas.estado import Estado, EstadoCreate, EstadoUpdate
from app.db.models.otros import Estado as EstadoModel
from app.db.models.usuario import UserRole
from app.db.session import get_db

router = APIRouter()

allowed_roles = [
    UserRole.ADMIN_CONSULTORA,
    UserRole.RESPONSABLE_HABILITACIONES,
    UserRole.OPERADOR_CONSULTORA,
    UserRole.EMPRESA,
]
access_required = RoleChecker(allowed_roles)


@router.get("/", response_model=List[Estado], dependencies=[Depends(access_required)])
async def list_estados(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EstadoModel))
    return result.scalars().all()


@router.post("/", response_model=Estado, status_code=status.HTTP_201_CREATED, dependencies=[Depends(access_required)])
async def create_estado(payload: EstadoCreate, db: AsyncSession = Depends(get_db)):
    estado = EstadoModel(**payload.model_dump())
    db.add(estado)
    await db.commit()
    await db.refresh(estado)
    return estado


@router.get("/{estado_id}", response_model=Estado, dependencies=[Depends(access_required)])
async def get_estado(estado_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EstadoModel).where(EstadoModel.id == estado_id))
    estado = result.scalar_one_or_none()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado


@router.patch("/{estado_id}", response_model=Estado, dependencies=[Depends(access_required)])
async def patch_estado(estado_id: int, payload: EstadoUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EstadoModel).where(EstadoModel.id == estado_id))
    estado = result.scalar_one_or_none()
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")

    changes = payload.model_dump(exclude_unset=True)
    for key, value in changes.items():
        setattr(estado, key, value)

    await db.commit()
    await db.refresh(estado)
    return estado

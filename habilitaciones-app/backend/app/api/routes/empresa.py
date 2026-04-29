from typing import List

from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import RoleChecker
from app.api.schemas.documento import Documento
from app.api.schemas.persona import Persona
from app.db.models.usuario import UserRole, Usuario
from app.db.session import get_db
from app.domain.documentos.repository import DocumentoRepository
from app.domain.documentos.service import DocumentoService
from app.domain.personas.repository import PersonaRepository
from app.domain.personas.service import PersonaService

router = APIRouter()

empresa_required = RoleChecker([UserRole.EMPRESA])


async def get_persona_service(db: AsyncSession = Depends(get_db)) -> PersonaService:
    return PersonaService(PersonaRepository(db))


async def get_documento_service(db: AsyncSession = Depends(get_db)) -> DocumentoService:
    return DocumentoService(DocumentoRepository(db), PersonaRepository(db))


@router.get("/personas", response_model=List[Persona])
async def get_empresa_personas(
    current_user: Usuario = Depends(empresa_required),
    service: PersonaService = Depends(get_persona_service),
):
    return await service.list_personas(current_user)


@router.post("/documentos", response_model=Documento)
async def upload_empresa_documento(
    persona_id: int = Form(...),
    tipo: str = Form(...),
    jurisdiccion: str = Form(...),
    fecha_presentacion: str = Form(...),
    file: UploadFile = File(...),
    current_user: Usuario = Depends(empresa_required),
    service: DocumentoService = Depends(get_documento_service),
):
    return await service.upload_documento(
        persona_id=persona_id,
        tipo=tipo,
        jurisdiccion=jurisdiccion,
        fecha_presentacion=fecha_presentacion,
        file=file,
        current_user=current_user,
    )

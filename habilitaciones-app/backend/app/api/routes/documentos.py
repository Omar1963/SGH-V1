from typing import List
from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import FileResponse

from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.db.models.documento import EstadoDocumento
from app.api.dependencies.auth import get_current_user, RoleChecker
from app.api.schemas.documento import Documento, DocumentoUpdate
from app.domain.documentos.repository import DocumentoRepository
from app.domain.documentos.service import DocumentoService
from app.domain.personas.repository import PersonaRepository

router = APIRouter()

# Roles permitidos
allowed_roles = [
    UserRole.ADMIN_CONSULTORA, 
    UserRole.RESPONSABLE_HABILITACIONES, 
    UserRole.OPERADOR_CONSULTORA,
    UserRole.EMPRESA
]
access_required = RoleChecker(allowed_roles)

async def get_documento_service(db: AsyncSession = Depends(get_db)) -> DocumentoService:
    repo = DocumentoRepository(db)
    persona_repo = PersonaRepository(db)
    return DocumentoService(repo, persona_repo)

@router.get("/", response_model=List[Documento])
async def list_documentos(
    current_user: Usuario = Depends(access_required),
    service: DocumentoService = Depends(get_documento_service)
):
    return await service.list_documentos(current_user)

@router.post("/upload", response_model=Documento, status_code=status.HTTP_201_CREATED)
async def upload_documento(
    persona_id: int = Form(...),
    tipo: str = Form(...),
    jurisdiccion: str = Form(...),
    fecha_presentacion: str = Form(...),
    file: UploadFile = File(...),
    current_user: Usuario = Depends(access_required),
    service: DocumentoService = Depends(get_documento_service)
):
    return await service.upload_documento(
        persona_id=persona_id,
        tipo=tipo,
        jurisdiccion=jurisdiccion,
        fecha_presentacion=fecha_presentacion,
        file=file,
        current_user=current_user
    )

@router.get("/{doc_id}", response_model=Documento)
async def get_documento(
    doc_id: int,
    current_user: Usuario = Depends(access_required),
    service: DocumentoService = Depends(get_documento_service)
):
    return await service.get_documento_secured(doc_id, current_user)

@router.get("/{doc_id}/download")
async def download_documento(
    doc_id: int,
    current_user: Usuario = Depends(access_required),
    service: DocumentoService = Depends(get_documento_service)
):
    doc = await service.get_documento_secured(doc_id, current_user)
    if not doc.path_archivo:
        raise HTTPException(status_code=404, detail="Archivo no encontrado para este documento")
    
    return FileResponse(path=doc.path_archivo, filename=f"documento_{doc_id}")

@router.put("/{doc_id}/status", response_model=Documento)
async def update_documento_status(
    doc_id: int,
    nuevo_estado: EstadoDocumento,
    current_user: Usuario = Depends(access_required),
    service: DocumentoService = Depends(get_documento_service)
):
    return await service.update_status(doc_id, nuevo_estado, current_user)

import os
import uuid
import aiofiles
from typing import List, Optional
from fastapi import HTTPException, status, UploadFile
from app.core.config import settings
from app.db.models.documento import Documento, EstadoDocumento
from app.db.models.usuario import Usuario, UserRole
from app.domain.documentos.repository import DocumentoRepository
from app.domain.personas.repository import PersonaRepository

class DocumentoService:
    def __init__(self, repository: DocumentoRepository, persona_repo: PersonaRepository):
        self.repository = repository
        self.persona_repo = persona_repo

    async def list_documentos(self, current_user: Usuario) -> List[Documento]:
        # Si es EMPRESA, solo ve documentos de personas de su empresa
        persona_ids = None
        if current_user.rol == UserRole.EMPRESA:
            personas = await self.persona_repo.get_all(empresa_id=current_user.empresa_id)
            persona_ids = [p.id for p in personas]
            if not persona_ids:
                return []
        
        return await self.repository.get_all(persona_ids=persona_ids)

    async def upload_documento(
        self, 
        persona_id: int, 
        tipo: str, 
        jurisdiccion: str, 
        fecha_presentacion: str,
        file: UploadFile,
        current_user: Usuario
    ) -> Documento:
        # Validar permisos sobre la persona
        persona = await self.persona_repo.get_by_id(persona_id)
        if not persona:
            raise HTTPException(status_code=404, detail="Persona no encontrada")
        
        if current_user.rol == UserRole.EMPRESA and persona.empresa_id != current_user.empresa_id:
            raise HTTPException(status_code=403, detail="No tiene permisos para esta persona")

        # Guardar archivo físico
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(settings.UPLOAD_DIR, unique_filename)
        
        # Crear directorio si no existe (back-up)
        if not os.path.exists(settings.UPLOAD_DIR):
            os.makedirs(settings.UPLOAD_DIR)

        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

        # Determinar estado inicial segun flujo maestro:
        # Empresa carga -> PENDIENTE_EMPRESA
        # Carga interna consultora -> PENDIENTE_REVISION
        if current_user.rol == UserRole.EMPRESA:
            estado = EstadoDocumento.PENDIENTE_EMPRESA
        else:
            estado = EstadoDocumento.PENDIENTE_REVISION

        doc_data = {
            "persona_id": persona_id,
            "tipo": tipo,
            "jurisdiccion": jurisdiccion,
            "fecha_presentacion": fecha_presentacion,
            "path_archivo": file_path,
            "estado": estado
        }
        
        return await self.repository.create(doc_data)

    async def get_documento_secured(self, doc_id: int, current_user: Usuario) -> Documento:
        doc = await self.repository.get_by_id(doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Documento no encontrado")
        
        # Validar pertenencia para empresas
        if current_user.rol == UserRole.EMPRESA:
            if doc.persona.empresa_id != current_user.empresa_id:
                 raise HTTPException(status_code=403, detail="Sin acceso al documento")
        
        return doc

    async def update_status(self, doc_id: int, nuevo_estado: EstadoDocumento, current_user: Usuario) -> Documento:
        # Solo roles de consultora pueden cambiar estados de revisión
        if current_user.rol not in [UserRole.ADMIN_CONSULTORA, UserRole.RESPONSABLE_HABILITACIONES, UserRole.OPERADOR_CONSULTORA]:
            raise HTTPException(status_code=403, detail="Acción no permitida")

        doc = await self.repository.get_by_id(doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Documento no encontrado")

        valid_transitions = {
            EstadoDocumento.PENDIENTE_EMPRESA: {EstadoDocumento.PENDIENTE_REVISION},
            EstadoDocumento.PENDIENTE_REVISION: {EstadoDocumento.APROBADO, EstadoDocumento.RECHAZADO},
            EstadoDocumento.APROBADO: {EstadoDocumento.VENCIDO},
            EstadoDocumento.RECHAZADO: {EstadoDocumento.PENDIENTE_EMPRESA},
            EstadoDocumento.VENCIDO: set(),
        }

        current_state = doc.estado
        if nuevo_estado == current_state:
            return doc

        if nuevo_estado not in valid_transitions.get(current_state, set()):
            raise HTTPException(
                status_code=400,
                detail=f"Transicion invalida: {current_state} -> {nuevo_estado}",
            )

        return await self.repository.update(doc_id, {"estado": nuevo_estado})

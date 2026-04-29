import asyncio
from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from app.db.models.documento import EstadoDocumento
from app.db.models.usuario import UserRole
from app.domain.documentos.service import DocumentoService


class DummyRepo:
    def __init__(self, doc):
        self.doc = doc
        self.updated_to = None

    async def get_by_id(self, _doc_id):
        return self.doc

    async def update(self, _doc_id, payload):
        self.updated_to = payload["estado"]
        self.doc.estado = payload["estado"]
        return self.doc


class DummyPersonaRepo:
    async def get_by_id(self, _persona_id):
        return SimpleNamespace(id=1, empresa_id=10)

    async def get_all(self, empresa_id=None):
        if empresa_id == 10:
            return [SimpleNamespace(id=1, empresa_id=10)]
        return []


def test_empresa_cannot_update_status():
    repo = DummyRepo(SimpleNamespace(id=1, estado=EstadoDocumento.PENDIENTE_EMPRESA))
    service = DocumentoService(repo, DummyPersonaRepo())
    empresa_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=10)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(service.update_status(1, EstadoDocumento.PENDIENTE_REVISION, empresa_user))

    assert exc.value.status_code == 403


def test_valid_transition_pendiente_empresa_to_revision():
    doc = SimpleNamespace(id=1, estado=EstadoDocumento.PENDIENTE_EMPRESA)
    repo = DummyRepo(doc)
    service = DocumentoService(repo, DummyPersonaRepo())
    admin_user = SimpleNamespace(rol=UserRole.ADMIN_CONSULTORA, empresa_id=None)

    updated = asyncio.run(service.update_status(1, EstadoDocumento.PENDIENTE_REVISION, admin_user))

    assert repo.updated_to == EstadoDocumento.PENDIENTE_REVISION
    assert updated.estado == EstadoDocumento.PENDIENTE_REVISION


def test_invalid_transition_pendiente_empresa_to_aprobado():
    doc = SimpleNamespace(id=1, estado=EstadoDocumento.PENDIENTE_EMPRESA)
    repo = DummyRepo(doc)
    service = DocumentoService(repo, DummyPersonaRepo())
    admin_user = SimpleNamespace(rol=UserRole.ADMIN_CONSULTORA, empresa_id=None)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(service.update_status(1, EstadoDocumento.APROBADO, admin_user))

    assert exc.value.status_code == 400

import asyncio
from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from app.db.models.usuario import UserRole
from app.domain.personas.service import PersonaService
from app.domain.documentos.service import DocumentoService
from app.domain.habilitaciones.service import HabilitacionService


class DummyPersonaRepo:
    def __init__(self, personas=None):
        self.personas = personas or []
        self.last_empresa_id = None

    async def get_all(self, empresa_id=None):
        self.last_empresa_id = empresa_id
        if empresa_id is None:
            return self.personas
        return [p for p in self.personas if p.empresa_id == empresa_id]

    async def get_by_id(self, persona_id):
        for persona in self.personas:
            if persona.id == persona_id:
                return persona
        return None

    async def create(self, payload):
        return SimpleNamespace(**payload)


class DummyDocumentoRepo:
    def __init__(self, documento=None):
        self.documento = documento

    async def get_by_id(self, doc_id):
        return self.documento


class DummyHabilitacionRepo:
    def __init__(self, habilitacion=None):
        self.habilitacion = habilitacion

    async def get_by_id(self, hab_id):
        return self.habilitacion


def test_empresa_personas_are_scoped_to_empresa_id():
    personas = [
        SimpleNamespace(id=1, empresa_id=22),
        SimpleNamespace(id=2, empresa_id=33),
    ]
    service = PersonaService(DummyPersonaRepo(personas=personas))
    current_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)

    result = asyncio.run(service.list_personas(current_user))

    assert len(result) == 1
    assert result[0].empresa_id == 22


def test_empresa_documento_access_is_denied_for_foreign_persona():
    doc = SimpleNamespace(id=1, persona=SimpleNamespace(empresa_id=99))
    service = DocumentoService(DummyDocumentoRepo(documento=doc), DummyPersonaRepo())
    current_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(service.get_documento_secured(1, current_user))

    assert exc.value.status_code == 403


def test_empresa_habilitacion_access_is_denied_for_foreign_persona():
    hab = SimpleNamespace(id=1, persona=SimpleNamespace(empresa_id=99))
    service = HabilitacionService(DummyHabilitacionRepo(habilitacion=hab), DummyPersonaRepo())
    current_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(service.get_habilitacion_secured(1, current_user))

    assert exc.value.status_code == 403


def test_empresa_create_persona_forces_own_empresa_id():
    repo = DummyPersonaRepo()
    service = PersonaService(repo)
    current_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)
    persona_in = SimpleNamespace(
        nombre="Test",
        apellido="User",
        dni="12345678",
        cuil="20-11111111-1",
        empresa_id=99,
        model_dump=lambda: {
            "nombre": "Test",
            "apellido": "User",
            "dni": "12345678",
            "cuil": "20-11111111-1",
            "empresa_id": 99,
        },
    )

    created = asyncio.run(service.create_persona(persona_in, current_user))

    assert created.empresa_id == 22

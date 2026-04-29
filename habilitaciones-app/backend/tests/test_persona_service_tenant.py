import asyncio
from types import SimpleNamespace

import pytest

from app.db.models.usuario import UserRole
from app.domain.personas.service import PersonaService


class DummyPersonaRepo:
    def __init__(self):
        self.called_empresa_id = None

    async def get_all(self, empresa_id=None):
        self.called_empresa_id = empresa_id
        return []

    async def get_by_cuil(self, _cuil):
        return None

    async def create(self, payload):
        return SimpleNamespace(**payload)


def test_empresa_list_personas_is_scoped_by_empresa_id():
    repo = DummyPersonaRepo()
    service = PersonaService(repo)
    empresa_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)

    asyncio.run(service.list_personas(empresa_user))

    assert repo.called_empresa_id == 22


def test_empresa_create_persona_forces_own_empresa_id():
    repo = DummyPersonaRepo()
    service = PersonaService(repo)
    empresa_user = SimpleNamespace(rol=UserRole.EMPRESA, empresa_id=22)
    persona_in = SimpleNamespace(
        cuil="20-11111111-1",
        model_dump=lambda: {
            "nombre": "Test",
            "apellido": "Persona",
            "dni": "12345678",
            "cuil": "20-11111111-1",
            "empresa_id": 999,
        },
    )

    created = asyncio.run(service.create_persona(persona_in, empresa_user))

    assert created.empresa_id == 22

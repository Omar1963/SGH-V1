# backend/tests/test_personas.py
"""Integration test for Persona creation.

- Endpoint: POST /api/personal/
- Role: Admin (JWT token)
- Expected initial state: PENDIENTE_REVISION
- Runs against Docker containers (requires the services to be up).
"""

import asyncio
import json
import os
from httpx import AsyncClient
import pytest

# Import FastAPI app for testing (adjust import if needed)
from backend.app.main import app

# Helper to create a JWT token for Admin role (uses the project's security utilities)
from backend.app.core.security import create_access_token
from backend.app.core import settings

# Fixture to ensure the database is seeded with a company and an admin user
@pytest.fixture(scope="module")
async def seed_data():
    # Assuming there is a function to create a company and an admin user directly via ORM.
    # This uses the repository layer to avoid HTTP calls.
    from backend.app.db.session import SessionLocal
    from backend.app.domain.empresa.repository import EmpresaRepository
    from backend.app.domain.usuario.repository import UsuarioRepository
    from backend.app.domain.empresa.models import Empresa
    from backend.app.domain.usuario.models import Usuario, RoleEnum

    db = SessionLocal()
    try:
        # Create a company if not exists
        empresa_repo = EmpresaRepository(db)
        empresa = await empresa_repo.get_by_name("TestEmpresa")
        if not empresa:
            empresa = Empresa(nombre="TestEmpresa")
            db.add(empresa)
            await db.flush()
        # Create an admin user for the company
        usuario_repo = UsuarioRepository(db)
        admin_user = await usuario_repo.get_by_email("admin@test.com")
        if not admin_user:
            admin_user = Usuario(
                email="admin@test.com",
                hashed_password="$2b$12$dummyhash",  # password not needed for token generation
                rol=RoleEnum.ADMIN,
                empresa_id=empresa.id,
            )
            db.add(admin_user)
            await db.flush()
        db.commit()
    finally:
        db.close()

    # Return company id for use in tests
    return empresa.id

# Fixture to obtain a JWT token for the admin user
@pytest.fixture(scope="module")
def admin_token(seed_data):
    # Payload must include user id, role and empresa_id as used by the project
    payload = {
        "sub": "admin@test.com",
        "role": "ADMIN",
        "empresa_id": seed_data,
    }
    token = create_access_token(data=payload, expires_delta=3600)
    return token

@pytest.mark.asyncio
async def test_create_persona(admin_token, seed_data):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        # Prepare request payload with required fields
        payload = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "dni": "12345678",
            "empresa_id": seed_data,
            "tipo_habilitacion": "NORMAL",  # adjust to actual enum value
        }
        headers = {
            "Authorization": f"Bearer {admin_token}",
            "Content-Type": "application/json",
        }
        response = await client.post("/api/personal/", json=payload, headers=headers)
        assert response.status_code == 201, f"Unexpected status: {response.status_code}, body: {response.text}"
        data = response.json()
        # Verify the returned persona contains the expected state
        assert data.get("estado") == "PENDIENTE_REVISION", "Persona not in expected state"
        # Basic field checks
        assert data.get("nombre") == "Juan"
        assert data.get("apellido") == "Pérez"
        assert data.get("dni") == "12345678"

# Note: To run this test against Docker containers, ensure that the containers are up
# and the environment variable `DATABASE_URL` points to the container's PostgreSQL instance.
# The test uses the FastAPI app directly, which will connect to the database defined
# in the Docker compose network.

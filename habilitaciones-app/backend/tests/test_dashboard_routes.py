import asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.main import app
from app.db.base import Base
from app.db.models.empresa import Empresa
from app.db.models.persona import Persona
from app.db.models.usuario import Usuario, UserRole
from app.db.models.dashboard import Dashboard
from app.api.dependencies.auth import get_current_user, get_db


def create_test_engine():
    return create_async_engine("sqlite+aiosqlite:///:memory:", echo=False, future=True)


async def build_route_test_context():
    engine = create_test_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with session_maker() as session:
        empresa = Empresa(cuit="12345678901", razon_social="Empresa Test", jurisdiccion="CABA")
        session.add(empresa)
        await session.flush()

        usuario = Usuario(
            usuario="empresa_user",
            contraseña_hash="testhash",
            rol=UserRole.EMPRESA,
            empresa_id=empresa.id,
        )
        session.add(usuario)
        await session.flush()

        dashboard = Dashboard(
            nombre="Dashboard ruta",
            descripcion="Dashboard para pruebas",
            visibilidad="PRIVATE",
            owner_id=usuario.id,
            empresa_id=empresa.id,
        )
        session.add(dashboard)
        await session.flush()

        await session.commit()

    return engine, session_maker, usuario, dashboard.id


def test_dashboard_routes_create_and_query():
    async def run():
        engine, session_maker, usuario, dashboard_id = await build_route_test_context()

        async def override_get_db():
            async with session_maker() as session:
                yield session

        async def override_get_current_user():
            return usuario

        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[get_current_user] = override_get_current_user

        client = TestClient(app)

        response = client.post(
            "/api/v1/dashboard/builder",
            json={
                "nombre": "Ruta test",
                "descripcion": "Creado por test",
                "visibilidad": "PRIVATE",
                "widgets": [],
                "filters": [],
            },
        )
        assert response.status_code == 201
        assert response.json()["nombre"] == "Ruta test"

        list_response = client.get("/api/v1/dashboard/builder")
        assert list_response.status_code == 200
        assert isinstance(list_response.json(), list)
        assert any(item["nombre"] == "Ruta test" for item in list_response.json())

        query_response = client.post(f"/api/v1/dashboard/builder/{dashboard_id}/query", json={})
        assert query_response.status_code == 200
        assert query_response.json()["dashboard_id"] == dashboard_id

        app.dependency_overrides.clear()

    asyncio.run(run())


def test_dashboard_routes_foreign_empresa_access_denied():
    async def run():
        engine, session_maker, usuario, dashboard_id = await build_route_test_context()

        async with session_maker() as session:
            empresa2 = Empresa(cuit="10987654321", razon_social="Otra Empresa", jurisdiccion="CABA")
            session.add(empresa2)
            await session.flush()

            other_user = Usuario(
                usuario="foreign_user",
                contraseña_hash="testhash",
                rol=UserRole.EMPRESA,
                empresa_id=empresa2.id,
            )
            session.add(other_user)
            await session.commit()

        async def override_get_db():
            async with session_maker() as session:
                yield session

        async def override_get_current_user():
            return other_user

        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[get_current_user] = override_get_current_user

        client = TestClient(app)
        response = client.get(f"/api/v1/dashboard/builder/{dashboard_id}")
        assert response.status_code == 404

        app.dependency_overrides.clear()

    asyncio.run(run())

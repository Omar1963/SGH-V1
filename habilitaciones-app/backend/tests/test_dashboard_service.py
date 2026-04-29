import asyncio
from datetime import date, timedelta
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.db.base import Base
from app.db.models.empresa import Empresa
from app.db.models.persona import Persona
from app.db.models.usuario import Usuario, UserRole
from app.db.models.otros import Habilitacion
from app.domain.dashboard.service import DashboardService
from app.api.schemas.dashboard import DashboardCreate, DashboardWidgetCreate


def create_test_engine():
    return create_async_engine("sqlite+aiosqlite:///:memory:", echo=False, future=True)


async def build_test_context():
    engine = create_test_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    session = session_maker()

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

    persona = Persona(
        dni="12345678",
        cuil="20123456789",
        nombre="Juan",
        apellido="Perez",
        empresa_id=empresa.id,
    )
    session.add(persona)
    await session.flush()

    habilitacion_vigente = Habilitacion(
        persona_id=persona.id,
        jurisdiccion="CABA",
        numero_credencial="A001",
        fecha_desde=date.today(),
        fecha_hasta=date.today() + timedelta(days=30),
        estado="VIGENTE",
    )
    habilitacion_por_vencer = Habilitacion(
        persona_id=persona.id,
        jurisdiccion="CABA",
        numero_credencial="A002",
        fecha_desde=date.today(),
        fecha_hasta=date.today() + timedelta(days=5),
        estado="POR_VENCER",
    )
    session.add_all([habilitacion_vigente, habilitacion_por_vencer])
    await session.commit()

    return engine, session, usuario


def test_dashboard_service_query_counts_by_estado():
    async def run():
        engine, session, usuario = await build_test_context()
        service = DashboardService(session)

        payload = DashboardCreate(
            nombre="Dashboard de prueba",
            descripcion="Resumen de habilitaciones",
            visibilidad="PRIVATE",
            widgets=[
                DashboardWidgetCreate(
                    tipo="kpi",
                    dataset_key="habilitaciones",
                    metric="count",
                    dimension="estado",
                    agregacion="count",
                )
            ],
            filters=[],
        )

        dashboard = await service.create_dashboard(usuario, payload)
        result = await service.query_dashboard(dashboard.id)

        assert result.message == "Consulta ejecutada correctamente."
        assert len(result.results) == 1
        chart = result.results[0]
        assert chart["dataset_key"] == "habilitaciones"
        assert chart["metric"] == "count"
        assert isinstance(chart["results"], list)
        labels = {row["label"] for row in chart["results"]}
        assert labels == {"VIGENTE", "POR_VENCER"}

        await session.close()
        await engine.dispose()

    asyncio.run(run())


def test_dashboard_service_lists_dashboards_for_empresa():
    async def run():
        engine, session, usuario = await build_test_context()
        service = DashboardService(session)

        payload = DashboardCreate(
            nombre="Dashboard de prueba",
            descripcion="Resumen de habilitaciones",
            visibilidad="PRIVATE",
            widgets=[],
            filters=[],
        )

        await service.create_dashboard(usuario, payload)
        dashboards = await service.get_dashboards(usuario)

        assert len(dashboards) == 1
        assert dashboards[0].nombre == "Dashboard de prueba"
        assert dashboards[0].empresa_id == usuario.empresa_id

        await session.close()
        await engine.dispose()

    asyncio.run(run())

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Creación del engine asíncrono usando la URL configurada
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=False,
    future=True,
    pool_pre_ping=True
)

# Constructor de sesiones asíncronas
SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    """
    Dependencia para obtener una sesión de base de datos asíncrona.
    """
    async with SessionLocal() as session:
        yield session

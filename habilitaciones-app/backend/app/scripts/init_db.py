import asyncio
from app.db.base import Base
from app.db.session import engine

async def init_db():
    async with engine.begin() as conn:
        # La clase Base en app.db.base ya importa todos los modelos
        # Así que Base.metadata ya tiene toda la información necesaria.
        await conn.run_sync(Base.metadata.create_all)
    print("Base de datos inicializada")

if __name__ == "__main__":
    asyncio.run(init_db())

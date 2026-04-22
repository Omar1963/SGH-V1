import asyncio
from app.db.base import Base  # Importar Base primero registra todos los modelos
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import SessionLocal
from app.db.models.usuario import Usuario, UserRole
from app.db.models.empresa import Empresa
from app.core.security import get_password_hash
from sqlalchemy import select

async def seed():
    async with SessionLocal() as db:
        # 1. Crear Empresa de prueba
        res_emp = await db.execute(select(Empresa).filter(Empresa.razon_social == "Empresa Test"))
        empresa = res_emp.scalar_one_or_none()
        if not empresa:
            empresa = Empresa(razon_social="Empresa Test", cuit="20-12345678-9", jurisdiccion="CABA")
            db.add(empresa)
            await db.commit()
            await db.refresh(empresa)
            print(f"Empresa creada: {empresa.id}")

        # 2. Crear Admin
        res_admin = await db.execute(select(Usuario).filter(Usuario.usuario == "admin@sgh.com"))
        admin = res_admin.scalar_one_or_none()
        if not admin:
            admin = Usuario(
                usuario="admin@sgh.com",
                contraseña_hash=get_password_hash("admin123"),
                rol=UserRole.ADMIN_CONSULTORA
            )
            db.add(admin)
            print("Admin creado")

        # 3. Crear Usuario Empresa
        res_user = await db.execute(select(Usuario).filter(Usuario.usuario == "test@empresa.com"))
        user = res_user.scalar_one_or_none()
        if not user:
            user = Usuario(
                usuario="test@empresa.com",
                contraseña_hash=get_password_hash("test123"),
                rol=UserRole.EMPRESA,
                empresa_id=empresa.id
            )
            db.add(user)
            print("Usuario Empresa creado")

        await db.commit()
        print("Seed completado")

if __name__ == "__main__":
    asyncio.run(seed())

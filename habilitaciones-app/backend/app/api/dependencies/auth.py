from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.config import settings
from app.core.security import ALGORITHM
from app.db.session import get_db
from app.db.models.usuario import Usuario, UserRole
from app.api.schemas.token import TokenPayload

# Definición del esquema OAuth2
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> Usuario:
    """
    Inyección de dependencia para validar el token y retornar el usuario actual.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, Exception):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No se pudo validar el access token.",
        )
    
    # Buscar usuario en DB
    result = await db.execute(select(Usuario).where(Usuario.usuario == token_data.sub))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    
    return user

class RoleChecker:
    """
    Clase para verificar si el usuario tiene uno de los roles permitidos.
    """
    def __init__(self, allowed_roles: List[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Usuario = Depends(get_current_user)):
        if user.rol not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operación no permitida para este rol."
            )
        return user

from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models.usuario import Usuario
from app.core import security
from app.core.config import settings
from app.api.schemas.token import Token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_access_token(
    db: AsyncSession = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    # Buscar usuario
    result = await db.execute(select(Usuario).where(Usuario.usuario == form_data.username))
    user = result.scalar_one_or_none()
    
    if not user or not security.verify_password(form_data.password, user.contraseña_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.usuario, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

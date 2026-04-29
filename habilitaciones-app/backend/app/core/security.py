from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Union
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# Contexto para hashing de contraseñas (PBKDF2 para mayor compatibilidad local)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

ALGORITHM = "HS256"

def create_access_token(
    subject: Union[str, Any],
    expires_delta: timedelta = None,
    extra_claims: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Genera un token JWT de acceso.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {"exp": expire, "sub": str(subject)}
    if extra_claims:
        to_encode.update(extra_claims)
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        # Hash desconocido/corrupto u otro error de passlib:
        # se trata como credencial inválida para evitar 500 en login.
        return False

def get_password_hash(password: str) -> str:
    """
    Genera el hash de una contraseña.
    """
    return pwd_context.hash(password)

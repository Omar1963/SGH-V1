from typing import List, Union, Any
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "SGH-V1"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/dbname"
    POSTGRES_SERVER: str = "db"
    POSTGRES_USER: str = "sgh_user"
    POSTGRES_PASSWORD: str = "sgh_password"
    POSTGRES_DB: str = "sgh_db"
    POSTGRES_PORT: int = 5432
    
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        # Si el servidor es 'db' (Docker) y no hay conexión, se podría fallar.
        # Para pruebas locales en Windows, si no hay POSTGRES_SERVER real, usamos SQLite.
        if self.POSTGRES_SERVER == "db":
             # Intento de detección: si no estamos en Docker, usar SQLite
             import os
             if not os.path.exists("/.dockerenv"):
                 return "sqlite+aiosqlite:///./test.db"
        
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # CORE SETTINGS
    SECRET_KEY: str = "SUPER_SECRET_KEY_CHANGEME"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    
    BACKEND_CORS_ORIGINS: Union[List[str], str] = []
    
    # Directorio para almacenamiento de archivos
    UPLOAD_DIR: str = "uploads"

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Any) -> Any:
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                try:
                    import json
                    return json.loads(v)
                except Exception:
                    pass
            # Caso común: "url1,url2"
            return [i.strip().rstrip("/") for i in v.split(",") if i.strip()]
        elif isinstance(v, list):
            return [str(i).rstrip("/") for i in v]
        return v

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()

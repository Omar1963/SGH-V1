from fastapi import APIRouter
from app.api.routes import auth, empresas, personas, documentos, habilitaciones, dashboard

api_router = APIRouter()

# Inclusión de routers por módulo
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
api_router.include_router(personas.router, prefix="/personas", tags=["personas"])
api_router.include_router(documentos.router, prefix="/documentos", tags=["documentos"])
api_router.include_router(habilitaciones.router, prefix="/habilitaciones", tags=["habilitaciones"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

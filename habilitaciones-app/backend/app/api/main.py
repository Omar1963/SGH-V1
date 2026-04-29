from fastapi import APIRouter
from app.api.routes import (
    alertas,
    auth,
    dashboard,
    documentos,
    empresa,
    empresas,
    estados,
    habilitaciones,
    personas,
    reportes,
)

api_router = APIRouter()

# Inclusión de routers por módulo
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
api_router.include_router(personas.router, prefix="/personas", tags=["personas"])
api_router.include_router(documentos.router, prefix="/documentos", tags=["documentos"])
api_router.include_router(estados.router, prefix="/estados", tags=["estados"])
api_router.include_router(habilitaciones.router, prefix="/habilitaciones", tags=["habilitaciones"])
api_router.include_router(alertas.router, prefix="/alertas", tags=["alertas"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(reportes.router, prefix="/reportes", tags=["reportes"])
api_router.include_router(empresa.router, prefix="/empresa", tags=["empresa"])

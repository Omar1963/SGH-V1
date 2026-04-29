from datetime import date
from typing import Any

from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_current_user
from app.db.models.usuario import Usuario

router = APIRouter()


@router.get("/{tipo}")
async def get_reporte(tipo: str, _current_user: Usuario = Depends(get_current_user)) -> Any:
    # Contrato minimo para etapa 2.4: endpoint disponible y tipado.
    return {
        "tipo": tipo,
        "generado_en": date.today().isoformat(),
        "estado": "DISPONIBLE",
        "items": [],
    }


@router.post("/{tipo}/pdf")
async def generar_reporte_pdf(tipo: str, _current_user: Usuario = Depends(get_current_user)) -> Any:
    return {
        "tipo": tipo,
        "estado": "GENERADO",
        "formato": "pdf",
        "url": None,
    }

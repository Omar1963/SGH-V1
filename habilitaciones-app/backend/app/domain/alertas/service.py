from datetime import date, timedelta
from typing import List, Dict
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.otros import Alerta, Habilitacion
from app.db.models.documento import Documento, EstadoDocumento
from app.db.models.usuario import Usuario, UserRole
from app.api.schemas.alerta import DashboardSummary
from app.domain.personas.repository import PersonaRepository

class AlertaService:
    def __init__(self, db: AsyncSession, persona_repo: PersonaRepository):
        self.db = db
        self.persona_repo = persona_repo

    async def get_dashboard_summary(self, current_user: Usuario) -> DashboardSummary:
        """
        Calcula el resumen para el dashboard filtrado por empresa si corresponde.
        """
        persona_ids = None
        if current_user.rol == UserRole.EMPRESA:
            personas = await self.persona_repo.get_all(empresa_id=current_user.empresa_id)
            persona_ids = [p.id for p in personas]
            if not persona_ids:
                return DashboardSummary(
                    habilitaciones_vigentes=0,
                    habilitaciones_por_vencer=0,
                    habilitaciones_vencidas=0,
                    alertas_activas=0,
                    documentos_pendientes_revision=0
                )

        # Consultas de contadores
        # Habilitaciones
        query_hab = select(Habilitacion.estado, func.count(Habilitacion.id)).group_by(Habilitacion.estado)
        if persona_ids is not None:
            query_hab = query_hab.where(Habilitacion.persona_id.in_(persona_ids))
        
        res_hab = await self.db.execute(query_hab)
        hab_counts = dict(res_hab.all())

        # Documentos pendientes de revision
        query_doc = select(func.count(Documento.id)).where(Documento.estado == EstadoDocumento.PENDIENTE_REVISION)
        if persona_ids is not None:
            query_doc = query_doc.where(Documento.persona_id.in_(persona_ids))
        
        res_doc = await self.db.execute(query_doc)
        doc_pending = res_doc.scalar() or 0

        # Alertas activas
        query_alerta = select(func.count(Alerta.id)).where(Alerta.estado == "ACTIVA")
        if persona_ids is not None:
            query_alerta = query_alerta.where(Alerta.persona_id.in_(persona_ids))
        
        res_alerta = await self.db.execute(query_alerta)
        alert_active = res_alerta.scalar() or 0

        # Mapeo a esquema final
        return DashboardSummary(
            habilitaciones_vigentes=hab_counts.get("VIGENTE", 0),
            habilitaciones_por_vencer=hab_counts.get("POR_VENCER", 0),
            habilitaciones_vencidas=hab_counts.get("VENCIDO", 0),
            alertas_activas=alert_active,
            documentos_pendientes_revision=doc_pending
        )

    async def refresh_alerts(self, current_user: Usuario):
        """
        Lógica para regenerar alertas basadas en fechas de vencimiento.
        (Ejecución manual inicial, escalable a cron job).
        """
        # TODO: Implementar lógica de escaneo de fechas < 30 días
        pass

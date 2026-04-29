from datetime import date
from typing import Any, List
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.db.models.otros import Habilitacion, Alerta
from app.db.models.documento import Documento
from app.db.models.persona import Persona
from app.db.models.usuario import Usuario, UserRole
from app.domain.dashboard.repository import DashboardRepository
from app.api.schemas.dashboard import (
    DashboardCatalog,
    DashboardCreate,
    DashboardUpdate,
    DashboardWidgetCreate,
    DashboardWidgetUpdate,
    DashboardFilterBase,
    DashboardShareCreate,
    DashboardQueryResult,
)

class DashboardService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = DashboardRepository(db)

    async def get_dashboard_catalog(self) -> DashboardCatalog:
        return DashboardCatalog(
            datasets=["habilitaciones", "alertas", "documentos"],
            metrics=["count", "sum", "avg"],
            dimensions=["estado", "tipo", "empresa", "fecha"],
            chart_types=["kpi", "line", "bar", "pie", "table"],
        )

    async def get_dashboards(self, current_user: Usuario) -> List[Any]:
        return await self.repo.list_for_user(current_user)

    async def create_dashboard(self, current_user: Usuario, payload: DashboardCreate) -> Any:
        dashboard_data = {
            "nombre": payload.nombre,
            "descripcion": payload.descripcion,
            "visibilidad": payload.visibilidad or "PRIVATE",
            "owner_id": current_user.id,
            "empresa_id": current_user.empresa_id,
        }
        dashboard = await self.repo.create(dashboard_data)

        for widget in payload.widgets:
            await self.repo.add_widget({
                "dashboard_id": dashboard.id,
                "tipo": widget.tipo,
                "dataset_key": widget.dataset_key,
                "metric": widget.metric,
                "dimension": widget.dimension,
                "agregacion": widget.agregacion,
                "orden": widget.orden or 0,
                "config": widget.config or {},
            })

        for filtro in payload.filters:
            await self.repo.create_filter({
                "dashboard_id": dashboard.id,
                "widget_id": filtro.widget_id,
                "campo": filtro.campo,
                "operador": filtro.operador,
                "valor": filtro.valor,
                "scope": filtro.scope or "dashboard",
            })

        return await self.repo.get_by_id(dashboard.id)

    async def create_dashboard(self, current_user: Usuario, payload: DashboardCreate) -> Any:
        dashboard_data = {
            "nombre": payload.nombre,
            "descripcion": payload.descripcion,
            "visibilidad": payload.visibilidad or "PRIVATE",
            "owner_id": current_user.id,
            "empresa_id": current_user.empresa_id,
        }
        dashboard = await self.repo.create(dashboard_data)

        for widget in payload.widgets:
            await self.repo.add_widget({
                "dashboard_id": dashboard.id,
                "tipo": widget.tipo,
                "dataset_key": widget.dataset_key,
                "metric": widget.metric,
                "dimension": widget.dimension,
                "agregacion": widget.agregacion,
                "orden": widget.orden or 0,
                "config": widget.config or {},
            })

        for filtro in payload.filters:
            await self.repo.create_filter({
                "dashboard_id": dashboard.id,
                "widget_id": filtro.widget_id,
                "campo": filtro.campo,
                "operador": filtro.operador,
                "valor": filtro.valor,
                "scope": filtro.scope or "dashboard",
            })

        return await self.repo.get_by_id(dashboard.id)

    async def get_dashboard(self, current_user: Usuario, dashboard_id: int) -> Any:
        dashboard = await self.repo.get_by_id(dashboard_id)
        if not dashboard:
            return None
        if current_user.rol == UserRole.EMPRESA and dashboard.empresa_id != current_user.empresa_id:
            return None
        return dashboard

    async def update_dashboard(self, dashboard_id: int, payload: DashboardUpdate) -> Any:
        update_data = {}
        if payload.nombre is not None:
            update_data["nombre"] = payload.nombre
        if payload.descripcion is not None:
            update_data["descripcion"] = payload.descripcion
        if payload.visibilidad is not None:
            update_data["visibilidad"] = payload.visibilidad
        if not update_data:
            return await self.repo.get_by_id(dashboard_id)
        return await self.repo.update(dashboard_id, update_data)

    async def add_widget(self, dashboard_id: int, payload: DashboardWidgetCreate) -> Any:
        return await self.repo.add_widget({
            "dashboard_id": dashboard_id,
            "tipo": payload.tipo,
            "dataset_key": payload.dataset_key,
            "metric": payload.metric,
            "dimension": payload.dimension,
            "agregacion": payload.agregacion,
            "orden": payload.orden or 0,
            "config": payload.config or {},
        })

    async def update_widget(self, widget_id: int, payload: DashboardWidgetUpdate) -> Any:
        update_data = {k: v for k, v in payload.model_dump(exclude_unset=True).items()}
        return await self.repo.update_widget(widget_id, update_data)

    async def delete_widget(self, widget_id: int) -> None:
        await self.repo.delete_widget(widget_id)

    async def query_dashboard(self, dashboard_id: int) -> DashboardQueryResult:
        dashboard = await self.repo.get_by_id(dashboard_id)
        if not dashboard:
            return DashboardQueryResult(
                dashboard_id=dashboard_id,
                results=[],
                message="Dashboard no encontrado.",
            )

        if not dashboard.widgets:
            return DashboardQueryResult(
                dashboard_id=dashboard.id,
                results=[],
                message="El dashboard no tiene widgets definidos.",
            )

        results = []
        for widget in sorted(dashboard.widgets, key=lambda item: item.orden or 0):
            results.append(await self._execute_widget_query(widget, dashboard.filters or []))

        return DashboardQueryResult(
            dashboard_id=dashboard.id,
            results=results,
            message="Consulta ejecutada correctamente.",
        )

    async def _execute_widget_query(self, widget: Any, filters: List[DashboardFilterBase]) -> dict[str, Any]:
        dataset_key = widget.dataset_key.lower()

        if widget.metric.lower() != "count":
            return {
                "widget_id": widget.id,
                "dataset_key": widget.dataset_key,
                "metric": widget.metric,
                "dimension": widget.dimension,
                "title": f"{widget.metric.upper()} no soportado",
                "results": [],
                "message": "Solo se soporta la métrica 'count' en esta versión.",
            }

        if dataset_key == "habilitaciones":
            rows = await self._query_habilitaciones(widget, filters)
        elif dataset_key == "alertas":
            rows = await self._query_alertas(widget, filters)
        elif dataset_key == "documentos":
            rows = await self._query_documentos(widget, filters)
        else:
            rows = []

        return {
            "widget_id": widget.id,
            "tipo": widget.tipo,
            "dataset_key": widget.dataset_key,
            "metric": widget.metric,
            "dimension": widget.dimension,
            "title": self._build_widget_title(widget),
            "results": rows,
        }

    async def _query_habilitaciones(self, widget: Any, filters: List[DashboardFilterBase]) -> List[dict[str, Any]]:
        if widget.dimension == "estado":
            stmt = select(Habilitacion.estado.label("label"), func.count(Habilitacion.id).label("value")).group_by(Habilitacion.estado)
        elif widget.dimension == "empresa":
            stmt = select(Persona.empresa_id.label("label"), func.count(Habilitacion.id).label("value")).join(Persona, Habilitacion.persona_id == Persona.id).group_by(Persona.empresa_id)
        elif widget.dimension == "fecha":
            stmt = select(func.date(Habilitacion.fecha_desde).label("label"), func.count(Habilitacion.id).label("value")).group_by(func.date(Habilitacion.fecha_desde))
        else:
            stmt = select(func.count(Habilitacion.id).label("value"))

        stmt = self._apply_filters(stmt, Habilitacion, filters, widget)
        result = await self.db.execute(stmt)
        return self._rows_to_list(result)

    async def _query_alertas(self, widget: Any, filters: List[DashboardFilterBase]) -> List[dict[str, Any]]:
        if widget.dimension == "estado":
            stmt = select(Alerta.estado.label("label"), func.count(Alerta.id).label("value")).group_by(Alerta.estado)
        elif widget.dimension == "tipo":
            stmt = select(Alerta.tipo.label("label"), func.count(Alerta.id).label("value")).group_by(Alerta.tipo)
        elif widget.dimension == "empresa":
            stmt = select(Persona.empresa_id.label("label"), func.count(Alerta.id).label("value")).join(Persona, Alerta.persona_id == Persona.id).group_by(Persona.empresa_id)
        elif widget.dimension == "fecha":
            stmt = select(func.date(Alerta.fecha).label("label"), func.count(Alerta.id).label("value")).group_by(func.date(Alerta.fecha))
        else:
            stmt = select(func.count(Alerta.id).label("value"))

        stmt = self._apply_filters(stmt, Alerta, filters, widget)
        result = await self.db.execute(stmt)
        return self._rows_to_list(result)

    async def _query_documentos(self, widget: Any, filters: List[DashboardFilterBase]) -> List[dict[str, Any]]:
        if widget.dimension == "estado":
            stmt = select(Documento.estado.label("label"), func.count(Documento.id).label("value")).group_by(Documento.estado)
        elif widget.dimension == "tipo":
            stmt = select(Documento.tipo.label("label"), func.count(Documento.id).label("value")).group_by(Documento.tipo)
        elif widget.dimension == "empresa":
            stmt = select(Persona.empresa_id.label("label"), func.count(Documento.id).label("value")).join(Persona, Documento.persona_id == Persona.id).group_by(Persona.empresa_id)
        elif widget.dimension == "fecha":
            stmt = select(func.date(Documento.fecha_presentacion).label("label"), func.count(Documento.id).label("value")).group_by(func.date(Documento.fecha_presentacion))
        else:
            stmt = select(func.count(Documento.id).label("value"))

        stmt = self._apply_filters(stmt, Documento, filters, widget)
        result = await self.db.execute(stmt)
        return self._rows_to_list(result)

    def _apply_filters(self, stmt: Any, model: Any, filters: List[DashboardFilterBase], widget: Any) -> Any:
        selected_filters = [
            filtro for filtro in filters
            if filtro.widget_id is None or filtro.widget_id == widget.id
        ]

        for filtro in selected_filters:
            field = filtro.campo
            operator = filtro.operador
            value = filtro.valor
            if value is None:
                continue

            if field == "empresa":
                stmt = stmt.join(Persona, model.persona_id == Persona.id)
                column = Persona.empresa_id
            else:
                column = getattr(model, field, None)

            if column is None:
                continue

            if operator == "equals":
                stmt = stmt.where(column == value)
            elif operator == "contains" and isinstance(value, str):
                stmt = stmt.where(column.ilike(f"%{value}%"))
            elif operator == "gt":
                stmt = stmt.where(column > value)
            elif operator == "lt":
                stmt = stmt.where(column < value)
            elif operator == "gte":
                stmt = stmt.where(column >= value)
            elif operator == "lte":
                stmt = stmt.where(column <= value)
            else:
                stmt = stmt.where(column == value)

        return stmt

    def _rows_to_list(self, result: Any) -> List[dict[str, Any]]:
        rows = []
        for row in result:
            mapping = row._mapping
            label = mapping.get("label") if "label" in mapping else "total"
            value = mapping.get("value")
            rows.append({"label": label, "value": value})
        return rows

    def _build_widget_title(self, widget: Any) -> str:
        title = f"{widget.metric.upper()} {widget.dataset_key}"
        if widget.dimension:
            title += f" por {widget.dimension}"
        return title

    async def share_dashboard(self, dashboard_id: int, payload: DashboardShareCreate) -> Any:
        share_data = {
            "dashboard_id": dashboard_id,
            "target_user_id": payload.target_user_id,
            "target_role": payload.target_role,
            "target_empresa_id": payload.target_empresa_id,
            "permisos": payload.permisos or {},
        }
        return await self.repo.create_share(share_data)

from typing import Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload
from app.db.models.dashboard import (
    Dashboard,
    DashboardWidget,
    DashboardFilter,
    DashboardShare,
)
from app.db.models.usuario import UserRole

class DashboardRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, dashboard_data: dict[str, Any]) -> Dashboard:
        dashboard = Dashboard(**dashboard_data)
        self.db.add(dashboard)
        await self.db.commit()
        await self.db.refresh(dashboard)
        return dashboard

    async def get_by_id(self, dashboard_id: int) -> Optional[Dashboard]:
        result = await self.db.execute(
            select(Dashboard)
            .options(
                selectinload(Dashboard.widgets),
                selectinload(Dashboard.filters),
                selectinload(Dashboard.shares),
            )
            .where(Dashboard.id == dashboard_id)
        )
        return result.scalar_one_or_none()

    async def list_for_user(self, current_user: Any) -> List[Dashboard]:
        query = select(Dashboard).options(
            selectinload(Dashboard.widgets),
            selectinload(Dashboard.filters),
            selectinload(Dashboard.shares),
        )
        if getattr(current_user, 'rol', None) == UserRole.EMPRESA:
            query = query.where(Dashboard.empresa_id == current_user.empresa_id)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def update(self, dashboard_id: int, update_data: dict[str, Any]) -> Optional[Dashboard]:
        await self.db.execute(update(Dashboard).where(Dashboard.id == dashboard_id).values(**update_data))
        await self.db.commit()
        return await self.get_by_id(dashboard_id)

    async def add_widget(self, widget_data: dict[str, Any]) -> DashboardWidget:
        widget = DashboardWidget(**widget_data)
        self.db.add(widget)
        await self.db.commit()
        await self.db.refresh(widget)
        return widget

    async def get_widget(self, widget_id: int) -> Optional[DashboardWidget]:
        result = await self.db.execute(select(DashboardWidget).where(DashboardWidget.id == widget_id))
        return result.scalar_one_or_none()

    async def update_widget(self, widget_id: int, update_data: dict[str, Any]) -> Optional[DashboardWidget]:
        await self.db.execute(update(DashboardWidget).where(DashboardWidget.id == widget_id).values(**update_data))
        await self.db.commit()
        return await self.get_widget(widget_id)

    async def delete_widget(self, widget_id: int) -> None:
        await self.db.execute(delete(DashboardWidget).where(DashboardWidget.id == widget_id))
        await self.db.commit()

    async def create_filter(self, filter_data: dict[str, Any]) -> DashboardFilter:
        filtro = DashboardFilter(**filter_data)
        self.db.add(filtro)
        await self.db.commit()
        await self.db.refresh(filtro)
        return filtro

    async def delete_filters_for_dashboard(self, dashboard_id: int) -> None:
        await self.db.execute(delete(DashboardFilter).where(DashboardFilter.dashboard_id == dashboard_id))
        await self.db.commit()

    async def create_share(self, share_data: dict[str, Any]) -> DashboardShare:
        share = DashboardShare(**share_data)
        self.db.add(share)
        await self.db.commit()
        await self.db.refresh(share)
        return share

    async def get_shares_for_dashboard(self, dashboard_id: int) -> List[DashboardShare]:
        result = await self.db.execute(select(DashboardShare).where(DashboardShare.dashboard_id == dashboard_id))
        return result.scalars().all()

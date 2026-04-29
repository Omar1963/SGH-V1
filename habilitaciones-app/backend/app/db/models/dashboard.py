from datetime import date
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date, JSON
from app.db.declarative_base import Base

class DashboardTemplate(Base):
    __tablename__ = "dashboard_templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    version: Mapped[str] = mapped_column(String(50), nullable=False, default="1.0")
    contenido: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    created_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    updated_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)

class Dashboard(Base):
    __tablename__ = "dashboards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    visibilidad: Mapped[str] = mapped_column(String(50), nullable=False, default="PRIVATE")
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    empresa_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("empresas.id"), nullable=True)
    created_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    updated_at: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)

    owner: Mapped["Usuario"] = relationship("Usuario")
    empresa: Mapped[Optional["Empresa"]] = relationship("Empresa")
    widgets: Mapped[List["DashboardWidget"]] = relationship(
        "DashboardWidget",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )
    filters: Mapped[List["DashboardFilter"]] = relationship(
        "DashboardFilter",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )
    shares: Mapped[List["DashboardShare"]] = relationship(
        "DashboardShare",
        back_populates="dashboard",
        cascade="all, delete-orphan",
    )

class DashboardWidget(Base):
    __tablename__ = "dashboard_widgets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dashboard_id: Mapped[int] = mapped_column(Integer, ForeignKey("dashboards.id"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(60), nullable=False)
    dataset_key: Mapped[str] = mapped_column(String(100), nullable=False)
    metric: Mapped[str] = mapped_column(String(100), nullable=False)
    dimension: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    agregacion: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    orden: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    config: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True, default=dict)

    dashboard: Mapped["Dashboard"] = relationship("Dashboard", back_populates="widgets")

class DashboardFilter(Base):
    __tablename__ = "dashboard_filters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dashboard_id: Mapped[int] = mapped_column(Integer, ForeignKey("dashboards.id"), nullable=False)
    widget_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("dashboard_widgets.id"), nullable=True)
    campo: Mapped[str] = mapped_column(String(100), nullable=False)
    operador: Mapped[str] = mapped_column(String(50), nullable=False)
    valor: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    scope: Mapped[str] = mapped_column(String(50), nullable=False, default="dashboard")

    dashboard: Mapped["Dashboard"] = relationship("Dashboard", back_populates="filters")

class DashboardShare(Base):
    __tablename__ = "dashboard_shares"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dashboard_id: Mapped[int] = mapped_column(Integer, ForeignKey("dashboards.id"), nullable=False)
    target_user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=True)
    target_role: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    target_empresa_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("empresas.id"), nullable=True)
    permisos: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True, default=dict)

    dashboard: Mapped["Dashboard"] = relationship("Dashboard", back_populates="shares")

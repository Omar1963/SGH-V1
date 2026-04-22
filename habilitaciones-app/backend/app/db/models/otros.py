from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date
from datetime import date
from app.db.declarative_base import Base

class Habilitacion(Base):
    __tablename__ = "habilitaciones"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    persona_id: Mapped[int] = mapped_column(Integer, ForeignKey("personas.id"), nullable=False)
    jurisdiccion: Mapped[str] = mapped_column(String(100), nullable=False)
    numero_credencial: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha_desde: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_hasta: Mapped[date] = mapped_column(Date, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # Relación
    persona: Mapped["Persona"] = relationship("Persona", back_populates="habilitaciones")

class Estado(Base):
    __tablename__ = "estados"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    persona_id: Mapped[int] = mapped_column(Integer, ForeignKey("personas.id"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False) # Ej: Psicotécnico
    jurisdiccion: Mapped[str] = mapped_column(String(100), nullable=False)
    valor: Mapped[str] = mapped_column(String(100), nullable=False) # Ej: APTO
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    
    # Relación
    persona: Mapped["Persona"] = relationship("Persona", back_populates="estados")

class Alerta(Base):
    __tablename__ = "alertas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    persona_id: Mapped[int] = mapped_column(Integer, ForeignKey("personas.id"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    mensaje: Mapped[str] = mapped_column(String(500), nullable=False)
    estado: Mapped[str] = mapped_column(String(50), default="ACTIVA")
    
    # Relación
    persona: Mapped["Persona"] = relationship("Persona", back_populates="alertas")

class Auditoria(Base):
    __tablename__ = "auditoria"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    accion: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    ip: Mapped[str] = mapped_column(String(50), nullable=True)
    resultado: Mapped[str] = mapped_column(String(255), nullable=True)
    
    # Relación
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="acciones_auditoria")

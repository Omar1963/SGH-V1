from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import List, Optional
from app.db.declarative_base import Base

class Persona(Base):
    __tablename__ = "personas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dni: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    cuil: Mapped[str] = mapped_column(String(11), unique=True, index=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    
    empresa_id: Mapped[int] = mapped_column(Integer, ForeignKey("empresas.id"), nullable=False)
    
    # Relaciones
    empresa: Mapped["Empresa"] = relationship("Empresa", back_populates="personas")
    documentos: Mapped[List["Documento"]] = relationship("Documento", back_populates="persona")
    estados: Mapped[List["Estado"]] = relationship("Estado", back_populates="persona")
    habilitaciones: Mapped[List["Habilitacion"]] = relationship("Habilitacion", back_populates="persona")
    alertas: Mapped[List["Alerta"]] = relationship("Alerta", back_populates="persona")

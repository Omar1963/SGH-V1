from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List
from app.db.declarative_base import Base

class Empresa(Base):
    __tablename__ = "empresas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cuit: Mapped[str] = mapped_column(String(11), unique=True, index=True, nullable=False)
    razon_social: Mapped[str] = mapped_column(String(255), nullable=False)
    jurisdiccion: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # Relaciones
    personas: Mapped[List["Persona"]] = relationship("Persona", back_populates="empresa")
    usuarios: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="empresa")

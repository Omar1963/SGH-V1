import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Enum
from typing import Optional
from app.db.declarative_base import Base

class UserRole(str, enum.Enum):
    ADMIN_CONSULTORA = "ADMIN_CONSULTORA"
    RESPONSABLE_HABILITACIONES = "RESPONSABLE_HABILITACIONES"
    OPERADOR_CONSULTORA = "OPERADOR_CONSULTORA"
    EMPRESA = "EMPRESA"
    AUDITOR = "AUDITOR"

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    usuario: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    contraseña_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)
    
    empresa_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("empresas.id"), nullable=True)
    
    # Relaciones
    empresa: Mapped[Optional["Empresa"]] = relationship("Empresa", back_populates="usuarios")
    acciones_auditoria: Mapped[list["Auditoria"]] = relationship("Auditoria", back_populates="usuario")

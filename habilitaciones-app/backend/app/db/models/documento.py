import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date, Enum
from datetime import date
from app.db.declarative_base import Base

class EstadoDocumento(str, enum.Enum):
    PENDIENTE_EMPRESA = "PENDIENTE_EMPRESA"
    PENDIENTE_REVISION = "PENDIENTE_REVISION"
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"
    VENCIDO = "VENCIDO"

class Documento(Base):
    __tablename__ = "documentos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    persona_id: Mapped[int] = mapped_column(Integer, ForeignKey("personas.id"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    jurisdiccion: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha_presentacion: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_vencimiento: Mapped[date] = mapped_column(Date, nullable=True)
    estado: Mapped[EstadoDocumento] = mapped_column(
        Enum(EstadoDocumento), 
        default=EstadoDocumento.PENDIENTE_EMPRESA,
        nullable=False
    )
    
    # Path del archivo almacenado
    path_archivo: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # Relaciones
    persona: Mapped["Persona"] = relationship("Persona", back_populates="documentos")

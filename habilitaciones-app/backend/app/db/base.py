from app.db.declarative_base import Base

# Importamos todos los modelos aquí para que Alembic pueda detectarlos a través de Base.metadata
from app.db.models.empresa import Empresa
from app.db.models.persona import Persona
from app.db.models.documento import Documento
from app.db.models.otros import Habilitacion, Estado, Alerta, Auditoria
from app.db.models.dashboard import DashboardTemplate, Dashboard, DashboardWidget, DashboardFilter, DashboardShare
from app.db.models.usuario import Usuario

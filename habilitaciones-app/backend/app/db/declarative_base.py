from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Clase base declarativa centralizada para evitar importaciones circulares.
    """
    pass

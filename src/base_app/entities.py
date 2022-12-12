from sqlalchemy import Column, Boolean, DateTime
from database.connection import Base

class BaseEntitie(Base):
    __abstract__ = True
    
    ativo = Column(Boolean)
    data_criacao = Column(DateTime)
    data_modificacao = Column(DateTime)

 
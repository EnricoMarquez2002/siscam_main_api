from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import EmailStr,
from base_app.entities import BaseEntitie


class Usuario(BaseEntitie):
    __tablename__ = 'users_usuario'

    id_usuario = Column(String(100), primary_key=True)
    nome = Column(String(100))
    sobrenome = Column(EmailStr)
    hashed_password = Column(String(300), nullable=True)
    acess_token = Column(String(300), nullable=True)
    refresh_token = Column(String(300), nullable=True)
    cep = Column(ForeignKey('address_endereco.cep'))
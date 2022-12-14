from sqlalchemy import Column, String, ForeignKey, Integer
from base_app.entities import BaseEntitie
from sqlalchemy.orm import relationship
from users import entities
from cameras.entities import camera


class Endereco(BaseEntitie):
    __tablename__ = 'address_endereco'

    cep = Column(String, primary_key=True)
    cidade_id_id = Column(Integer, ForeignKey('address_cidade.cidade_id'))

    usuario = relationship("Usuario", back_populates="endereco")
    camera = relationship("Camera", back_populates="endereco")

    
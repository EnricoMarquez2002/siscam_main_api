from sqlalchemy import Column, Integer, String, ForeignKey
from base_app.entities import BaseEntitie


class Endereco(BaseEntitie):
    __tablename__ = 'address_endereco'

    cep = Column(String(100), primary_key=True)
    cidade_id = Column(ForeignKey('address_cidade.cidade_id'))
    
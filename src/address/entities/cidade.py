from sqlalchemy import Column, Integer, String, ForeignKey
from base_app.entities import BaseEntitie


class Cidade(BaseEntitie):
    __tablename__ = 'address_cidade'

    cidade_id = Column(Integer, auto_increment=True)
    cidade = Column(String(100))
    uf_id = Column(ForeignKey('address_uf.uf_id'))


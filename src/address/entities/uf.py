from sqlalchemy import Column, Integer, String
from base_app.entities import BaseEntitie


class Uf(BaseEntitie):
    __tablename__ = 'address_uf'

    uf_id = Column(Integer, auto_increment=True, primary_key=True)
    estado = Column(String)
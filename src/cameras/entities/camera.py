from sqlalchemy import Column, Integer, ForeignKey
from base_app.entities import BaseEntitie
from pydantic import AnyUrl


class Camera(BaseEntitie):
    __tablename__ = 'cameras_camera'

    id_camera = Column(Integer, auto_increment=True, primary_key=True)
    url_camera = Column(AnyUrl)
    cep = Column(ForeignKey('address_endereco.cep'))

    
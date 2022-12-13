from sqlalchemy import Column, Integer, ForeignKey, String
from base_app.entities import BaseEntitie
from sqlalchemy.orm import relationship
from address.entities import endereco


class Camera(BaseEntitie):
    __tablename__ = 'cameras_camera'

    id_camera = Column(Integer, auto_increment=True, primary_key=True)
    url_camera = Column(String(200))
    cep_id = Column(ForeignKey('address_endereco.cep'))

    endereco = relationship("Endereco", back_populates="camera")
    
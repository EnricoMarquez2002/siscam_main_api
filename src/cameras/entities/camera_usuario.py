from sqlalchemy import Column, Integer, ForeignKey, DateTime
from base_app.entities import BaseEntitie


class CameraUsuario(BaseEntitie):
    __tablename__ = 'cameras_camerausuario'

    id_camera_usuario = Column(Integer, auto_increment=True, primary_key=True)
    id_camera = Column(ForeignKey('cameras_camera.id_camera'))
    id_usuario = Column(ForeignKey('users_usuario.id_usuario'))
    data_uso = Column(DateTime)
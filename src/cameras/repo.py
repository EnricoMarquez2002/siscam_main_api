from database.config import DBConnectionHandler
from cameras.entities.camera import Camera
from cameras.entities import camera


class CameraRepo():

    @classmethod
    def read_by_address(cls, cep: int):
        with DBConnectionHandler() as db_connection:
            
            all_cameras = db_connection.session.query(
                camera.Camera.ativo,
                camera.Camera.url_camera,
                camera.Camera.cep_id
            )\
            .filter(camera.Camera.cep_id == cep)\
            .all()
        
            return all_cameras
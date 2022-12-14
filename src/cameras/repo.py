from database.config import DBConnectionHandler
from cameras.entities.camera import Camera
from cameras.entities import camera
from fastapi import HTTPException, status


class CameraRepo():

    @classmethod
    def read_by_address(cls, cep: str):
        with DBConnectionHandler() as db_connection:
            
            all_cameras = db_connection.session.query(
                camera.Camera.id_camera
            )\
            .filter(camera.Camera.cep_id == cep)\
            .all()
        
            return all_cameras

    @classmethod
    def read_camera(cls, id_camera: int):
        with DBConnectionHandler() as db_connection:

            camera_info = db_connection.session.query(
                camera.Camera.ativo,
                camera.Camera.data_criacao,
                camera.Camera.url_camera,
                camera.Camera.cep_id
            )\
            .filter(camera.Camera.id_camera == id_camera)\
            .first()

            if camera_info is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found")
            else:
                return camera_info
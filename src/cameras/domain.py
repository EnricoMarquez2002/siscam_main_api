from .repo import CameraRepo


class GetCamerasByAddressUseCase():

    def execute(cep: int):
        all_cameras = CameraRepo.read_by_address(cep)
        return all_cameras

class GetCameraByUrlUseCase():

    def execute(camera_url: str):
        camera_info = CameraRepo.read_camera(camera_url)
        return camera_info
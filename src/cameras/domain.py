from .repo import CameraRepo


class GetCamerasByAddressUseCase():

    def execute(cep: int):
        all_cameras = CameraRepo.read_by_address(cep)
        return all_cameras

class GetCameraByUrlUseCase():

    def execute(id_camera: int):
        return CameraRepo.read_camera(id_camera)
        
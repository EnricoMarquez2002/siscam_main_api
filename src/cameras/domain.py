from .repo import CameraRepo


class GetCamerasByAddressUseCase():

    def execute(cep: str):
        return CameraRepo.read_by_address(cep)

class GetCameraByUrlUseCase():

    def execute(id_camera: int):
        return CameraRepo.read_camera(id_camera)
        
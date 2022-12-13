from .repo import CameraRepo


class GetCameraByAddressUseCase():

    def execute(cep: int):
        all_cameras = CameraRepo.read_by_address(cep)
        return all_cameras
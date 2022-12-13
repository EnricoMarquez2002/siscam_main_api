from fastapi import APIRouter
from .domain import GetCamerasByAddressUseCase, GetCameraByUrlUseCase


router = APIRouter(
    prefix="/camera",
    tags= ["Cameras"]
)

@router.get('s/{cep}', status_code=200)
async def read_cameras_by_address(cep: int):
    all_cameras = GetCamerasByAddressUseCase.execute(cep)
    return all_cameras

@router.get('/{url_camera}', status_code=200)
async def read_camera_by_url(camera_url: str):
   camera_info = GetCameraByUrlUseCase.execute(camera_url)
   return camera_info

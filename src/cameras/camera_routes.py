from fastapi import APIRouter, Depends
from .domain import GetCamerasByAddressUseCase, GetCameraByUrlUseCase
from base_app.security.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/camera",
    tags= ["Cameras"],
    dependencies=[Depends(JWTBearer())]
)

@router.get('s/{cep}', status_code=200)
async def read_cameras_by_address(cep: int):
    all_cameras = GetCamerasByAddressUseCase.execute(cep)
    return all_cameras

@router.get('/{url_camera}', status_code=200)
async def read_camera_by_url(camera_url: str):
   camera_info = GetCameraByUrlUseCase.execute(camera_url)
   return camera_info

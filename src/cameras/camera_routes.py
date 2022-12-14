from fastapi import APIRouter, Depends
from .domain import GetCamerasByAddressUseCase, GetCameraByUrlUseCase
from base_app.security.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/camera",
    tags= ["Cameras"],
    dependencies=[Depends(JWTBearer())]
)

@router.get('s/{cep}', status_code=200)
async def read_cameras_by_address(cep: str):
    return GetCamerasByAddressUseCase.execute(cep)

@router.get('/{id_camera}', status_code=200)
async def read_camera_by_id(id_camera: int):
   return GetCameraByUrlUseCase.execute(id_camera)
  
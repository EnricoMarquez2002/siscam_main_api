from fastapi import APIRouter
from .domain import GetCameraByAddressUseCase


router = APIRouter(
    prefix="/cameras",
    tags= ["Cameras"]
)

@router.get('', status_code=200)
async def read_cameras_by_address(cep: int):
    all_cameras = GetCameraByAddressUseCase.execute(cep)
    return all_cameras
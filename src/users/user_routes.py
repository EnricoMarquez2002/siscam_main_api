from fastapi import APIRouter
from .domain import GetAllUsersUseCase


router = APIRouter(
    prefix='/users',
    tags= ['Users']
)

@router.get('', status_code=200)
async def get_all():
    all_users = GetAllUsersUseCase.execute()
    return all_users
    
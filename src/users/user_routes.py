from fastapi import APIRouter
from .domain import GetAllUsersUseCase, PostUserUseCase
from .models.user_post import UserModelPost


router = APIRouter(
    prefix='/user',
    tags= ['Users']
)

@router.get('s', status_code=200)
async def get_all():
    all_users = GetAllUsersUseCase.execute()
    return all_users

@router.post('', status_code=201)
async def create_user(user: UserModelPost):
    PostUserUseCase.execute(user)
    


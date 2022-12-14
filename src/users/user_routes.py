from fastapi import APIRouter, Depends
from .domain import GetAllUsersUseCase, PostUserUseCase, ReadMeUseCase
from .models.user_post import UserModelPost
from base_app.security.auth_bearer import JWTBearer


router = APIRouter(
    prefix='/user',
    tags= ['Users']
)

@router.get('s', status_code=200)
async def get_all():
    return GetAllUsersUseCase.execute()

@router.get('/me')
async def read_me(user: str = Depends(JWTBearer())):
    return ReadMeUseCase.execute(user)
    
@router.post('', status_code=201)
async def create_user(user: UserModelPost):
    return PostUserUseCase.execute(user)


    


from fastapi import APIRouter
from .domain import UserLoginUseCase, UserRefreshSessionUseCase
from pydantic import EmailStr
from .models.acess_token import AcessTokenModel


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/token')
async def authenticate(email: EmailStr, password: str):
    return UserLoginUseCase.execute(email, password)
    
@router.post('/refresh')
async def refresh_session(acess_token: str):
    return UserRefreshSessionUseCase.execute(acess_token)
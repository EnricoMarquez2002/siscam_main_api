from fastapi import APIRouter
from .domain import UserLoginUseCase
from pydantic import EmailStr


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/token')
async def authenticate(email: EmailStr, password: str):
    user = UserLoginUseCase.execute(email, password)
    return user
    
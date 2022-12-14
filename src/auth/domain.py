from fastapi import HTTPException, status
from.repo import AuthRepo
from pydantic import EmailStr
from base_app.security.bcrypt import verify_password
from base_app.security.auth_handler import create_acess_token, create_refresh_token
from .models.acess_token import AcessTokenModel
from jose import jwt
from base_app.security.auth_handler import JWT_SECRET, JWT_ALGORITHM


class UserLoginUseCase():

    def execute(email:EmailStr, password: str):
        user = AuthRepo.get_user_by_email(email)

        if user is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if verify_password(password, user.hashed_password):
            return create_acess_token(email, user.id_usuario)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

class UserRefreshSessionUseCase():
    def execute(acess_token: str):
        refresh = jwt.decode(acess_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if refresh:
            AuthRepo.get_user_by_token(acess_token)
            return create_acess_token(refresh.get("sub"), refresh.get("id")), create_refresh_token(refresh.get("sub"), refresh.get("lstn"))



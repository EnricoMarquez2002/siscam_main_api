from fastapi import HTTPException, status
from.repo import AuthRepo
from pydantic import EmailStr
from base_app.security.bcrypt import verify_password
from base_app.security.auth_handler import create_acess_token


class UserLoginUseCase():

    def execute(email:EmailStr, password: str):
        user = AuthRepo.user_login(email, password)

        print(user)

        if user is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if verify_password(password, user.hashed_password):
            return create_acess_token(email, user.id_usuario)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
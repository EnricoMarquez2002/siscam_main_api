from .repo import UsuarioRepo
from .models.user_post import UserModelPost
from fastapi import HTTPException, status


class GetAllUsersUseCase():

    def execute():
        all = UsuarioRepo.get_all()
        return all

class PostUserUseCase():

    def execute(user: UserModelPost):
        return UsuarioRepo.post_user(user)

class ReadMeUseCase():

    def execute(user: str):
        return UsuarioRepo.get_user_by_id(user)
            
            
                
        
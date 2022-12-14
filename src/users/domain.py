from .repo import UsuarioRepo
from .models.user_post import UserModelPost
from fastapi import HTTPException, status


class GetAllUsersUseCase():

    def execute():
        all = UsuarioRepo.get_all()
        return all

class PostUserUseCase():

    def execute(user: UserModelPost):
        UsuarioRepo.post_user(user)
            
            
                
        
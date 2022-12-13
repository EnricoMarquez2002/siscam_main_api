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
        
        if user.cep_id is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CEP not found")
        else:
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User created")
            
                
        
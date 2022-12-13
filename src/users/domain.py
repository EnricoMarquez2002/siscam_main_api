from .repo import UsuarioRepo


class GetAllUsersUseCase():

    def execute():
        all = UsuarioRepo.get_all()
        return all
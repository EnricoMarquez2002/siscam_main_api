from fastapi import HTTPException, status
from database.config import DBConnectionHandler
from users import entities
from .models.user_post import UserModelPost


class UsuarioRepo():

    @classmethod
    def get_all(cls):
        with DBConnectionHandler() as db_connection:

            all = db_connection.session.query(
                entities.Usuario.nome,
                entities.Usuario.sobrenome,
                entities.Usuario.email,
                entities.Usuario.cep_id
            )\
            .all()

            return all

    
            
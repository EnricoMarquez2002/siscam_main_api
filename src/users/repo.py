from fastapi import HTTPException, status
from database.config import DBConnectionHandler
from users import entities
from .models.user_post import UserModelPost
from base_app.security.bcrypt import get_password_hash
import datetime
import uuid


class UsuarioRepo():

    @classmethod
    def get_all(cls):
        with DBConnectionHandler() as db_connection:

            return  db_connection.session.query(
                entities.Usuario.nome,
                entities.Usuario.sobrenome,
                entities.Usuario.email,
                entities.Usuario.cep_id
            )\
            .all()

    @classmethod
    def get_user_by_id(cls, user: str):
        with DBConnectionHandler() as db_connection:

            return db_connection.session.query(
                entities.Usuario.data_criacao,
                entities.Usuario.nome,
                entities.Usuario.sobrenome,
                entities.Usuario.email,
                entities.Usuario.cep_id
            )\
            .filter(entities.Usuario.id_usuario == user)\
            .first()

    @classmethod
    def post_user(cls, user: UserModelPost):
        with DBConnectionHandler() as db_connection:

            new_user = entities.Usuario()
            new_user.ativo = True
            new_user.data_criacao = datetime.datetime.now()
            new_user.data_modificacao = datetime.datetime.now()
            new_user.id_usuario = uuid.uuid4()
            new_user.nome = user.nome.capitalize()
            new_user.sobrenome = user.sobrenome.capitalize()
            new_user.email = user.email

            hashed_password = get_password_hash(user.hashed_password)
            new_user.hashed_password = hashed_password

            new_user.cep_id = user.cep_id

            db_connection.session.add(new_user)
            db_connection.session.commit()

            return HTTPException(status_code=status.HTTP_201_CREATED, detail="User created")

    

            

            



            
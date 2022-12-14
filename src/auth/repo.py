from database.config import DBConnectionHandler
from pydantic import EmailStr
from users import entities
from .models.acess_token import AcessTokenModel


class AuthRepo():

    @classmethod
    def get_user_by_email(cls, email: EmailStr):
        with DBConnectionHandler() as db_connection:

         user = db_connection.session.query(entities.Usuario)\
        .filter(entities.Usuario.email == email)\
        .first()

        return user
    
    @classmethod
    def get_user_by_token(cls, acess_token: str):
        with DBConnectionHandler() as db_connection:

         user = db_connection.session.query(entities.Usuario)\
        .filter(entities.Usuario.acess_token == acess_token)\
        .first()

        return user

    @classmethod
    def update_acess_token(cls, email: EmailStr, token: str):
        with DBConnectionHandler() as db_connection:

            db_connection.session.query(entities.Usuario)\
            .filter(entities.Usuario.email == email)\
            .update({"acess_token": token})

            db_connection.session.commit()

    @classmethod
    def update_refresh_token(cls, email: EmailStr, refresh_token: str):
        with DBConnectionHandler() as db_connection:

            db_connection.session.query(entities.Usuario)\
            .filter(entities.Usuario.email == email)\
            .update({"refresh_token": refresh_token})

            db_connection.session.commit()

 
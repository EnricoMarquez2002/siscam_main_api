from database.config import DBConnectionHandler
from pydantic import EmailStr
from users import entities


class AuthRepo():

    @classmethod
    def user_login(cls, email: EmailStr, password: str):
        with DBConnectionHandler() as db_connection:

         user = db_connection.session.query(entities.Usuario)\
        .filter(entities.Usuario.email == email)\
        .first()

        return user

    @classmethod
    def update_acess_token(cls, email: EmailStr, token: str):
        with DBConnectionHandler() as db_connection:

            db_connection.session.query(entities.Usuario)\
            .filter(entities.Usuario.email == email)\
            .update({"acess_token": token})

            db_connection.session.commit()
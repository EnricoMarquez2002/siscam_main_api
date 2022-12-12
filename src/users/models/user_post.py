from .user_base import UserModelBase


class UserModelPost(UserModelBase):
    hashed_password: str
    cep: str

    class Config:
        schema_extra = {
            "example": {
                "nome": "nome",
                "sobrenome": "sobrenome",
                "email": "email@exemplo.com",
                "hashed_password": "senha",
                "cep": "12345-678"
            }
        }
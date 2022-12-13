from .user_base import UserModelBase
from typing import Optional


class UserModelPost(UserModelBase):
    hashed_password: str
    cep_id: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "nome": "nome",
                "sobrenome": "sobrenome",
                "email": "email@exemplo.com",
                "hashed_password": "senha",
                "cep_id": "12345-678"
            }
        }
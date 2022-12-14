from .user_base import UserModelBase
from typing import Optional
from pydantic import validator
import re


class UserModelPost(UserModelBase):
    hashed_password: str
    cep_id: str

    class Config:
        schema_extra = {
            "example": {
                "nome": "nome",
                "sobrenome": "sobrenome",
                "email": "email@exemplo.com",
                "hashed_password": "senha",
                "cep_id": "12345678"
            }
        }

    @validator('hashed_password')
    def validate_password(cls, value: str):
        if len(value) < 8:
            raise ValueError("Password must be longer tha 8 digits")
        if not re.search('[A-Z]', value):
            raise ValueError("Password must have at least one upper digit")
        if not re.search("[0-9]", value):
            raise ValueError("Password must have ate lesat one number")
        if not re.search(r"[ `!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~]", value):
            raise ValueError("Password must have at least one special digit")
        return value
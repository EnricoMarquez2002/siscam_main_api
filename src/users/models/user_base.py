from pydantic import BaseModel, EmailStr


class UserModelBase(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr

    class Config:
        orm_mode=True

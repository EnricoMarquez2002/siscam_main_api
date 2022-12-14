from pydantic import BaseModel


class AcessTokenModel(BaseModel):
    token: str
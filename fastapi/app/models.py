from pydantic import BaseModel


class ValidateTokenModel(BaseModel):
    token: str

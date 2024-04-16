from pydantic import Field
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()


class Settings(BaseSettings):
    user_name: str = Field(alias="USERNAME")
    host_name: str = Field(alias="HOSTNAME")
    public_key: str = Field(alias="PUBLICKEY")
    private_key: str = Field(alias="PRIVATEKEY")

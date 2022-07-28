from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    db_user_name:str
    db_name:str
    db_password:str
    host:str
    port : int
    access_token_expire_time: int
    algorithme:str
    class Config:
        env_file = ".env"

settings = Settings()
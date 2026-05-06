import secrets
from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config  = SettingsConfigDict(
        env_file= ".env",
        env_ignore_empty = True,
        extra = "ignore"
    )
    SECRET_KEY : str = secrets.token_urlsafe(32)
    DATABASE_URL: str
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60

settings = Settings() 
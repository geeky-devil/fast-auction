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
    LISTING_EXPIRE_SECONDS:int = 60 * 2
    LISTING_RESOLVE_SECONDS:int = 3
    LISTING_CLEAN_UP_SECONDS:int = 60 * 4

settings = Settings() 
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database settings
    POSTGRES_USER: str = "Postgres"
    POSTGRES_PASSWORD: str = "Postgres"
    POSTGRES_DB: str = "showu"
    POSTGRES_HOST: str = "127.0.0.1"
    POSTGRES_PORT: str = "5432"
    
    # Redis settings 
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: str = "6379"

    # Security settings
    SECRET_KEY: str = "super-secret-key-change-this"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True
    
        extra = "ignore" 

settings = Settings()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)
Base = declarative_base()

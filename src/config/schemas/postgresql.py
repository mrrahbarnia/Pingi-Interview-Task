from pydantic_settings import BaseSettings


class PostgreSQL(BaseSettings):
    USERNAME: str
    PASSWORD: str
    DATABASE_NAME: str
    HOST: str
    PORT: int

from pydantic_settings import BaseSettings


class Django(BaseSettings):
    DEBUG_MODE: bool
    SECRET_KEY: str

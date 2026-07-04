from pydantic_settings import BaseSettings, SettingsConfigDict

from . import schemas


class _ENVS(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
    )

    DJANGO: schemas.Django


ENVS = _ENVS()  # type: ignore

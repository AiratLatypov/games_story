from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


class AppConfig(BaseConfig):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DB_URL: str = Field(validation_alias="DB_URL")
    DEBUG: bool = Field(
        validation_alias="DEBUG",
        default=True,
    )


class Settings(BaseConfig):
    app: AppConfig = Field(default_factory=AppConfig)


settings = Settings()

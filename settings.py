from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "DevOps Starter API"
    app_env: str = "development"
    debug: bool = True
    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/devops_starter"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
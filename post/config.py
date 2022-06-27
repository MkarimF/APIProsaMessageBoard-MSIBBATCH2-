from pydantic import BaseSettings, validator


class DatabaseConfig(BaseSettings):
    url: str = "postgresql://postgres: @localhost/db_LandingPage"

    @validator("url")
    def fix_scheme(cls, v):
        return v.replace("postgres://", "postgresql://")

    class Config:
        env_prefix = "database_"
        env_file = ".env"

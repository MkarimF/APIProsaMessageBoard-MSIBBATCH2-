from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    url: str = "postgresql://postgres: @localhost/db_LandingPage"

    class Config:
        env_prefix = "database_"
        env_file = ".env"

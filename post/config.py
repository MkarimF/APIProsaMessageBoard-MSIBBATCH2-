from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    url: str = "postgresql://postgresql: @localhost/db_LandingPage"

    class Config:
        env_prefix = "database_"
        env_file = ".env"

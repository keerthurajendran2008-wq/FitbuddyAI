from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FitBuddy"
    database_url: str = "sqlite:///./fitbuddy.db"
    admin_token: str = "fitbuddy-admin"

    class Config:
        env_file = ".env"

settings = Settings()
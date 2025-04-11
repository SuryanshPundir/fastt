from typing import Optional
from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None

    class Config:
        env_file = ".env"

class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False

class DevConfig(GlobalConfig):
    class Config:
        env_prefix = "DEV_"

class TestConfig(GlobalConfig):
    class Config:
        env_prefix = "TEST_"

class ProdConfig(GlobalConfig):
    class Config:
        env_prefix = "PROD_"

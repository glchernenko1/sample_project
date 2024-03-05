from pydantic_settings import BaseSettings, SettingsConfigDict
from decimal import *


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    class SettingsDeposits:
        max_period: int = 60
        min_period: int = 1
        max_amount: Decimal = 1000000
        min_amount: Decimal = 10000
        max_rate: Decimal = 8
        min_rate: Decimal = 1
    # class Config: #todo заменить на
    #     env_file = '.env'
    #     env_file_encoding = 'utf-8'
    model_config = SettingsConfigDict(env_file=".env")
# settings = Settings(_env_file='../../.env')
settings = Settings()
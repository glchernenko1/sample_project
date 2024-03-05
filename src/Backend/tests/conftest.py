import pytest
from fastapi.testclient import TestClient # документация https://fastapi.tiangolo.com/ru/reference/testclient/?h=test
from src.Backend.app.settings import settings
from src.Backend.app.app import app

# defult settings
settings.SettingsDeposits.min_amount = 10000
settings.SettingsDeposits.max_amount = 1000000
settings.SettingsDeposits.min_period = 1
settings.SettingsDeposits.max_period = 60
settings.SettingsDeposits.min_rate = 1
settings.SettingsDeposits.max_rate = 8

client = TestClient(app)
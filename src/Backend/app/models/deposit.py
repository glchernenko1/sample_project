from fastapi import HTTPException
from pydantic import BaseModel, field_validator, Field, ValidationError
from datetime import date
from ..settings import settings
from decimal import *



class Deposit(BaseModel):
    st_date: date = Field(alias='date')
    period: int
    amount: Decimal
    rate: Decimal = Field(ge=settings.SettingsDeposits.min_rate, le=settings.SettingsDeposits.max_rate, description='Interest on deposit')


    @field_validator('st_date',mode='before')
    def date_validator(cls, v):
        try:
            date.fromisoformat(v)
            return v
        except ValueError:
            raise ValueError('Некоректная дата')


    @field_validator('period')
    def period_validator(cls, v):
        if v < settings.SettingsDeposits.min_period or v > settings.SettingsDeposits.max_period:
            raise ValueError(f'Периуд должен быть от {settings.SettingsDeposits.min_period } '
                                  f'до {settings.SettingsDeposits.max_period } месяцев')
        return v

    @field_validator('amount')
    def amount_validator(cls, v):
        if v < settings.SettingsDeposits.min_amount or v > settings.SettingsDeposits.max_amount:
            raise ValueError(f'Вклад должен быть от {settings.SettingsDeposits.min_amount} '
                                  f'до {settings.SettingsDeposits.max_amount}')
        return v

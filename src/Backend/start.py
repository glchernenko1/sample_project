import app.services.deposit as deposit
import app.models.deposit as deposit_model
import simplejson as json

from pydantic import BaseModel, field_validator, Field
from pydantic.dataclasses import dataclass

from datetime import date
# print(json.dumps(deposit.calculate_deposit(deposit_model.Deposit(st_date="2021-01-321", period=70, amount=10000, rate=6)), use_decimal=True))


class Deposit(BaseModel):
    st_date: date




    @field_validator('st_date',mode='before')
    def date_validator(cls, v):
        try:
            date.fromisoformat(v)
            return v
        except ValueError:
            raise ValueError('Некоректная дата')

print(Deposit(st_date="2021-01-011"))


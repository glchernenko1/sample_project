
from ..models.deposit import Deposit
from dateutil.relativedelta import relativedelta
from decimal import *
def calculate_deposit(deposit_data: Deposit)-> dict[str, Decimal]:
    """
    Calculate deposit
    :param deposit_data: Deposit
    :return: map[str][int]
    """
    current_deposit_amount = Decimal(deposit_data.amount)
    result = {}
    for i in range(deposit_data.period):
        current_deposit_amount *= (1 + deposit_data.rate / 100 / 12)
        result[str(deposit_data.st_date + relativedelta(months=i+1))] = current_deposit_amount
    return result



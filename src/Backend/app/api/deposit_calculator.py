from decimal import Decimal

from starlette.responses import JSONResponse

from ..models.deposit import Deposit
from ..services import deposit as deposit_service
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

router = APIRouter(
    prefix="/deposit",
    tags=["deposit"],
)


@router.post("/", response_model=dict[str, Decimal])
async def calculate_deposit(deposit_in: Deposit ) -> dict[str, Decimal]:
    try:
        result = deposit_service.calculate_deposit(deposit_in)
        return result
    except ValidationError  as e:
        error_messages = [f'Ошибка в поле {detail["loc"][1]} {detail["msg"]}' for detail in e.errors()]
        raise HTTPException(status_code=400, detail=f'error:  {error_messages} ')
from fastapi import APIRouter, Response

from app.service import PaymentInformationService
from app.schemas import PaymentInformation, User

payment_information_router = APIRouter()
payment_information_service = PaymentInformationService()


@payment_information_router.post("/api/v1/payment_information/{user_id}", response_model=User)
async def create_payment_information(user_id: str, payment_information: PaymentInformation, response: Response):
    response.status_code = 201
    return payment_information_service.create_payment_information(user_id, payment_information)


@payment_information_router.delete(
    "/api/v1/payment_information/{user_id}/id/{payment_information_id}",
    response_model=User
)
async def create_payment_information(user_id: str, payment_information_id: str):
    return payment_information_service.delete_payment_information(user_id, payment_information_id)

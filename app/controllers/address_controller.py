from fastapi import APIRouter, Response

from app.service import AddressService
from app.schemas import Address, User

address_router = APIRouter()
address_service = AddressService()


@address_router.post("/api/v1/address/{user_id}", response_model=User)
async def create_address(user_id: str, address: Address, response: Response):
    response.status_code = 201
    return address_service.create_address(user_id, address)


@address_router.delete("/api/v1/address/{user_id}/id/{address_id}", response_model=User)
async def create_address(user_id: str, address_id: str):
    return address_service.delete_address(user_id, address_id)

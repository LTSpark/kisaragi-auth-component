from fastapi import HTTPException, status

from app.schemas import CreateAddress
from app.repository import UserRepository, AddressRepository


class AddressService:

    user_repository = UserRepository
    address_repository = AddressRepository

    def create_address(self, user_id: str, address: CreateAddress):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        return self.address_repository.add_address_to_user(user, address).to_dict()

    def delete_address(self, user_id: str, address_id: str):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        address_list = user.addresses.filter(_id=address_id)
        if not address_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Address with id {address_id} not found"
            )

        address = address_list[0]
        return self.address_repository.remove_address_from_user(user, address).to_dict()

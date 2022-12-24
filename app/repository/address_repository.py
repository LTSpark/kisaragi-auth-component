from dotenv import load_dotenv

from app.models import User, Address
from app.internal import DatabaseConfig
from app.schemas import Address as AddressSchema

load_dotenv()
DatabaseConfig().connect_database()


class AddressRepository:

    @staticmethod
    def add_address_to_user(user: User, address: AddressSchema) -> User:
        address = Address(
            address=address.address,
            district=address.city,
            city=address.city,
            zipcode=address.zipcode
        )
        user.addresses.append(address)
        return user.save()

    @staticmethod
    def remove_address_from_user(user: User, address: Address) -> User:
        user.addresses.remove(address)
        return user.save()

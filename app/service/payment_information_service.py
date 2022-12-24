from fastapi import HTTPException, status

from app.schemas import PaymentInformation
from app.repository import UserRepository, PaymentInformationRepository


class PaymentInformationService:

    user_repository = UserRepository
    payment_information_repository = PaymentInformationRepository

    def create_payment_information(self, user_id: str, payment_information: PaymentInformation):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        return self.payment_information_repository.add_payment_information_to_user(user, payment_information).to_dict()

    def delete_payment_information(self, user_id: str, payment_information_id: str):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        payment_information_list = user.payment_information.filter(_id=payment_information_id)
        if not payment_information_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Payment Information with id {payment_information_id} not found"
            )

        payment_information = payment_information_list[0]
        return self.payment_information_repository.remove_payment_information_from_user(user, payment_information).to_dict()

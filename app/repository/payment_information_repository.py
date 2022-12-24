from dotenv import load_dotenv

from app.models import User, PaymentInformation
from app.internal import DatabaseConfig
from app.schemas.user_schema import PaymentInformation as PaymentInformationSchema

load_dotenv()
DatabaseConfig().connect_database()


class PaymentInformationRepository:

    @staticmethod
    def add_payment_information_to_user(user: User, payment_information: PaymentInformationSchema) -> User:
        payment_information = PaymentInformation(
            primary_account_number=payment_information.primary_account_number,
            cardholder_name=payment_information.cardholder_name,
            expiration_date=payment_information.expiration_date,
            active=True
        )
        user.payment_information.append(payment_information)
        return user.save()

    @staticmethod
    def remove_payment_information_from_user(user: User, payment_information: PaymentInformation) -> User:
        user.payment_information.remove(payment_information)
        return user.save()

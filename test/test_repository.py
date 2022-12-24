import datetime
import unittest

from app.repository import UserRepository, AddressRepository, PaymentInformationRepository
from app.schemas import CreateUser, CreateAddress, CreatePaymentInformation


class RepositoryUnitTest(unittest.TestCase):

    user_id = None

    user_repository = UserRepository
    address_repository = AddressRepository
    payment_information_repository = PaymentInformationRepository

    def test_01_create_user(self):
        user = CreateUser(
            user_name="mock_user",
            email="mock_user123@test.com",
            password="Test12345",
            telephone_number="123456789",
            birth_date=datetime.date.today(),
            role="USER",
        )
        created_user = self.user_repository.create_user(user)
        self.assertIsNotNone(created_user, "User was not created!")
        self.__class__.user_id = created_user.to_dict()['user_id']

    def test_02_get_user_by_id(self):
        user_id = self.__class__.user_id
        user = self.user_repository.get_user_by_id(user_id).to_dict()
        self.assertIsNotNone(user)
        self.assertEqual(user['user_id'], user_id)

    def test_03_get_user_by_name(self):
        user = self.user_repository.get_user_by_name("mock_user")
        self.assertEqual(user["user_name"], "mock_user")

    def test_04_get_user_by_email(self):
        user = self.user_repository.get_user_by_email("mock_user123@test.com").to_dict()
        self.assertEqual(user["email"], "mock_user@test.com")

    def test_05_add_address(self):
        user_id = self.__class__.user_id
        user = self.address_repository.add_address_to_user(
            self.user_repository.get_user_by_id(user_id),
            CreateAddress(
                address="Jr Prueba 231",
                city="Prueba City",
                zipcode="12345",
                district="District Prueba"
            )
        )

        self.assertIsNotNone(user.addresses[0])
        self.assertEqual(user.addresses[0].address, "Jr Prueba 231")

    def test_06_delete_address(self):
        user_test = self.user_repository.get_user_by_id(self.__class__.user_id)
        user = self.address_repository.remove_address_from_user(
            user_test,
            user_test.addresses[0]
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.addresses, [])

    def test_07_add_payment_info(self):
        user_id = self.__class__.user_id
        user = self.payment_information_repository.add_payment_information_to_user(
            self.user_repository.get_user_by_id(user_id),
            CreatePaymentInformation(
                primary_account_number="4557124234321413",
                cardholder_name="Prueba Cardholder",
                expiration_date=datetime.date.today(),
            )
        )

        self.assertIsNotNone(user.payment_information[0])
        self.assertEqual(user.payment_information[0].cardholder_name, "Prueba Cardholder")

    def test_08_remove_payment_info(self):
        user_test = self.user_repository.get_user_by_id(self.__class__.user_id)
        user = self.payment_information_repository.remove_payment_information_from_user(
            user_test,
            user_test.payment_information[0]
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.payment_information, [])

    def test_09_delete_user(self):
        user_id = self.__class__.user_id
        self.user_repository.delete_user(user_id)
        user = self.user_repository.get_user_by_id(user_id)
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()

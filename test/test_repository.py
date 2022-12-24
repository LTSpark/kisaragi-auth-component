import datetime
import unittest

from app.repository import UserRepository
from app.schemas import CreateUser

unittest.TestLoader.sortTestMethodsUsing = None


class RepositoryUnitTest(unittest.TestCase):

    user_id = None
    user_repository = UserRepository

    def test_01_create_user(self):
        user = CreateUser(
            user_name="mock_user",
            email="mock_user@test.com",
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
        user = self.user_repository.get_users_by_name("mock_user")[0]
        self.assertEqual(user["user_name"], "mock_user")

    def test_04_get_user_by_email(self):
        user = self.user_repository.get_user_by_email("mock_user@test.com").to_dict()
        self.assertEqual(user["email"], "mock_user@test.com")

    def test_05_delete_user(self):
        user_id = self.__class__.user_id
        self.user_repository.delete_user(user_id)
        user = self.user_repository.get_user_by_id(user_id)
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()

import re

from dotenv import load_dotenv
from datetime import datetime

from app.models import User
from app.schemas import CreateUser
from app.internal import DatabaseConfig

load_dotenv()
DatabaseConfig().connect_database()


class UserRepository:

    @staticmethod
    def create_user(user: CreateUser) -> User:
        return User(
            user_name=user.user_name,
            email=user.email,
            password=user.password,
            telephone_number=user.telephone_number,
            birth_date=user.birth_date,
            role=user.role
        ).save()

    @staticmethod
    def get_user_by_id(user_id) -> User:
        return User.objects(_id=user_id).first()

    @staticmethod
    def get_users_by_name(user_name) -> list[User]:
        users = []
        name_regex = re.compile(f'.*{user_name}*.', re.IGNORECASE)
        user_objs = User.objects(user_name=name_regex)
        for user_obj in user_objs:
            users.append(user_obj.to_dict())
        return users

    @staticmethod
    def get_user_by_email(user_email) -> User:
        return User.objects(email=user_email).first()

    @staticmethod
    def delete_user(user_id):
        User.objects(_id=user_id).delete()

    @staticmethod
    def update_user(user_id, name, surname, password, profile_image):
        User.objects(_id=user_id).update(
            set__name=name,
            set__surname=surname,
            set__password=password,
            set__profile_image=profile_image,
            set__updated_at=datetime.utcnow()
        )

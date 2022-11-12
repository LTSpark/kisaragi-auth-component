from datetime import datetime
from fastapi import HTTPException

from app.models import User
from app.schemas import CreateUser


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
        return User.objects(id=user_id).first()

    @staticmethod
    def get_user_by_name(user_name) -> User:
        return User.objects(name=user_name).first()

    @staticmethod
    def get_user_by_email(user_email) -> User:
        return User.objects(email=user_email).first()

    @staticmethod
    def delete_user(user_id):
        User.objects(id=user_id).first()

    @staticmethod
    def update_user(user_id, name, description, password, profile_image):
        User.objects(id=user_id).update(
            set__name=name,
            set__description=description,
            set__password=password,
            set__profile_image=profile_image,
            set__updated_at=datetime.utcnow()
        )

from datetime import datetime

from app.models import User


class UserRepository:

    @staticmethod
    def create_user(name, email, password, description, birth_date):
        new_user = User(
            name=name,
            email=email,
            description=description,
            password=password,
            birth_date=birth_date
        )
        new_user.save()

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects(id=user_id).first()

    @staticmethod
    def get_user_by_name(user_name):
        return User.objects(name=user_name).first()

    @staticmethod
    def get_user_by_email(user_email):
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

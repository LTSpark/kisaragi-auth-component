import bcrypt
from fastapi import HTTPException

from app.schemas import CreateUser
from app.repository import UserRepository


class UserService:

    user_repository = UserRepository

    def create_user(self, user: CreateUser):
        user.password = bcrypt.hashpw(
            user.password.encode('utf8'),
            bcrypt.gensalt()
        ).decode('utf8')
        try:
            self.user_repository.create_user(user)
            return {"msg": "User created successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=e.__str__())

    def get_user_by_email(self, email):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=404, detail=f"User with email {email} not found")
        return user.to_dict()

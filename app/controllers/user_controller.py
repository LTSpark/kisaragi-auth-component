import bcrypt
from fastapi import APIRouter

from app.service import UserService
from app.schemas import CreateUser, User

user_router = APIRouter()
user_service = UserService()


@user_router.post("api/v1/users")
async def create_user(user: CreateUser):
    return user_service.create_user(user)


@user_router.get("api/v1/users/{email}/email", response_model=User)
async def get_user_by_email(email: str):
    return user_service.get_user_by_email(email)

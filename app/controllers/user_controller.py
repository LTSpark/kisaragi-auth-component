from fastapi import APIRouter, Response

from app.service import UserService
from app.schemas import CreateUser, User, LoginUser

user_router = APIRouter()
user_service = UserService()


@user_router.post("/api/v1/users", response_model=LoginUser)
async def create_user(user: CreateUser, response: Response):
    response.status_code = 201
    return user_service.create_user(user)


@user_router.get("/api/v1/users/{email}/email", response_model=User)
async def get_user_by_email(email: str):
    return user_service.get_user_by_email(email)

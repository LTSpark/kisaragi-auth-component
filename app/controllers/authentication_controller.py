from fastapi import APIRouter

from app.service import UserService
from app.schemas import LoginUser, RequestLoginUser

auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/api/v1/auth", response_model=LoginUser)
async def login_user(user: RequestLoginUser):
    return user_service.login(user.email, user.password)

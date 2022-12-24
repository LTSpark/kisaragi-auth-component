from typing import Optional

from fastapi import APIRouter, Response, File, UploadFile, Form

from app.service import UserService
from app.schemas import CreateUser, User, LoginUser

user_router = APIRouter()
user_service = UserService()


@user_router.post("/api/v1/users", response_model=LoginUser)
async def create_user(user: CreateUser, response: Response):
    response.status_code = 201
    return user_service.create_user(user)


@user_router.put("/api/v1/users/{user_id}", response_model=User)
async def update_user(
        user_id: str,
        name: Optional[str] = Form(None),
        surname: Optional[str] = Form(None),
        password: Optional[str] = Form(None),
        file: Optional[UploadFile] = File(...)
):
    file_read = await file.read()
    return user_service.update(user_id, name, surname, file_read, password)


@user_router.get("/api/v1/users/{email}/email", response_model=User)
async def get_user_by_email(email: str):
    return user_service.get_user_by_email(email)


@user_router.get("/api/v1/users/{user_id}/id", response_model=User)
async def get_user_by_id(user_id: str):
    return user_service.get_user_by_id(user_id)


@user_router.get("/api/v1/users/{user_name}/name", response_model=User)
async def get_user_by_name(user_name: str):
    return user_service.get_user_by_name(user_name)


@user_router.delete("/api/v1/users/{user_id}/id")
async def delete(user_id: str):
    return user_service.delete(user_id)

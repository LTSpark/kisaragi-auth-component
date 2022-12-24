from fastapi import APIRouter

import os

from dotenv import load_dotenv


load_dotenv()

health_router = APIRouter()


@health_router.get("/api/v1/health")
async def health_check():
    return {"msg": "Everything is OK!", "status": "Healthy", "database": os.getenv("MONGODB_URI")}

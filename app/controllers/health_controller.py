from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/api/v1/health")
async def create_user():
    return {"msg": "Everything is OK!", "status": "Healthy"}

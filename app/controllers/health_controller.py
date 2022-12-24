from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/api/v1/health")
async def health_check():
    return {"msg": "Everything is OK!", "status": "Healthy"}

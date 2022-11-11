from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from app.internal import DatabaseConfig
from app.controllers import user_router

load_dotenv()

DatabaseConfig().connect_database()


tags_metadata = [
    {
        "name": "Users",
        "description": "Manage Users database operations.",
    },
    {
        "name": "Auth",
        "description": "Manage authorization processes, supports traditional OAuth.",
    },
    {
        "name": "Payment Information",
        "description": "Manage Users Payment Information database operations."
    }
]

app = FastAPI(
    title="Kisaragi Authentication Component",
    version="0.0.5",
    description="REST API for managing users authorization and personal information.",
    docs_url="/api/v1/documentation",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=["Users"])

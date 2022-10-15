from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [{
    "name": "User",
    "description": "Manage user database operations"
}, {
    "name": "Auth",
    "description": "Manage authorization processes"
}]

app = FastAPI(
    title="Kisaragi Authentication Component",
    description="REST API for managing user authorization and personal information",
    version="0.0.5",
    open_api_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

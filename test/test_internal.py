from fastapi.testclient import TestClient

from main import app
from app.internal import DatabaseConfig

from app.internal import authentication
from fastapi import Depends
from fastapi.security import HTTPBearer
from app.internal.logger import Logger


DatabaseConfig().connect_database()

client = TestClient(app)

def test_get_token_payload():
    security = HTTPBearer()
    response = authentication.get_token_payload(Depends(security))
    print(response)


def test_error():
    myLogger = Logger(__name__)
    myLogger.error(data={'message':'error test'})

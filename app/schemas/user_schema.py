from datetime import date, datetime
from typing import Union, Optional, List

from pydantic import BaseModel, Field


class PaymentInformation(BaseModel):
    payment_information_id: str
    primary_account_number: str
    cardholder_name: str
    expiration_date: date
    active: bool
    created_at: datetime
    updated_at: datetime


class User(BaseModel):
    user_id: str
    name: str
    email: str
    birth_date: date
    description: Optional[str] = None
    profile_image: Optional[str] = None
    payment_information: Optional[List[PaymentInformation]] = None
    created_at: datetime
    updated_at: datetime


class CreateUser(BaseModel):
    name: str = Field(
        title="Username",
        max_length=25,
        min_length=6
    )
    email: str = Field(
        title="Email of the user",
        regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    )
    password: str = Field(
        title="Password of the user",
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    )
    birth_date: date = None
    telephone_number: str = Field(
        title="User telephone number",
        min_length=9,
        max_length=9
    )
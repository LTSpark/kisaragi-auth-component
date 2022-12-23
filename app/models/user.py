from enum import Enum
from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import Document, StringField, ObjectIdField, EnumField, \
    EmailField, DateTimeField, EmbeddedDocumentListField, DateField

from app.models import PaymentInformation, Address


class Role(Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'


class User(Document):

    _id = ObjectIdField(required=True, default=ObjectId)

    user_name = StringField(unique=True, min_length=6, max_length=25, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)

    telephone_number = StringField(min_length=9, max_length=9, required=True)
    profile_image = StringField(required=False)
    birth_date = DateField(required=True)

    name = StringField()
    surname = StringField()

    role = EnumField(Role)
    addresses = EmbeddedDocumentListField(Address)
    payment_information = EmbeddedDocumentListField(PaymentInformation)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def get_id(self):
        return str(self._id)

    def to_dict(self):
        return {
            "user_id": str(self._id),
            "user_name": self.user_name,
            "email": self.email,
            "birth_date": self.birth_date,
            "profile_image": self.profile_image,
            "role": self.role.name,
            "telephone_number": self.telephone_number,
            "name": self.name,
            "surname": self.surname,
            "addresses": list(map(
                lambda addresses: addresses.to_dict(),
                self.addresses)
            ),
            "payment_information": list(map(
                lambda payment_information: payment_information.to_dict(),
                self.payment_information)
            ),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import Document, StringField, ObjectIdField, EmailField, DateTimeField, EmbeddedDocumentListField

from app.models import PaymentInformation


class User(Document):

    _id = ObjectIdField(required=True, default=ObjectId)

    name = StringField(unique=True, min_length=6, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    description = StringField(max_length=100, required=False)

    birth_date = DateTimeField()
    profile_image = StringField(required=True)

    payment_information = EmbeddedDocumentListField(PaymentInformation)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def to_dict(self):
        return {
            "user_id": str(self._id),
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "birth_date": self.birth_date,
            "profile_image": self.profile_image,
            "payment_information": list(map(
                lambda payment_information: payment_information.to_dict(),
                self.payment_information)
            ),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

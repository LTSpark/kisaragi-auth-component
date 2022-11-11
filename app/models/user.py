from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import Document, StringField, ObjectIdField, \
    EmailField, DateTimeField, EmbeddedDocumentListField, DateField

from app.models import PaymentInformation


class User(Document):

    _id = ObjectIdField(required=True, default=ObjectId)

    name = StringField(unique=True, min_length=6, max_length=25, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)

    telephone_number = StringField(min_length=9, max_length=9, required=True)
    profile_image = StringField(required=False)
    birth_date = DateField(required=True)

    payment_information = EmbeddedDocumentListField(PaymentInformation)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def to_dict(self):
        return {
            "user_id": str(self._id),
            "name": self.name,
            "email": self.email,
            "birth_date": self.birth_date,
            "profile_image": self.profile_image,
            "telephone_number": self.telephone_number,
            "payment_information": list(map(
                lambda payment_information: payment_information.to_dict(),
                self.payment_information)
            ),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

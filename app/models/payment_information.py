from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import EmbeddedDocument, StringField, DateTimeField, ObjectIdField


class PaymentInformation(EmbeddedDocument):

    _id = ObjectIdField(required=True, default=ObjectId)

    cardholder_name = StringField(required=True)
    primary_account_number = StringField(required=True)
    expiration_date = DateTimeField(required=True)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def to_dict(self):
        return {
            "payment_information_id": str(self._id),
            "primary_account_number": self.primary_account_number,
            "expiration_date": self.expiration_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

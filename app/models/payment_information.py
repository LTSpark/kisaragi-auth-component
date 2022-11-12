from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import EmbeddedDocument, StringField, DateTimeField, ObjectIdField, BooleanField, DateField


class PaymentInformation(EmbeddedDocument):

    _id = ObjectIdField(required=True, default=ObjectId)

    cardholder_name = StringField(required=True)
    primary_account_number = StringField(required=True)
    expiration_date = DateField(required=True)
    active = BooleanField(require=True)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def to_dict(self):
        return {
            "payment_information_id": str(self._id),
            "primary_account_number": self.primary_account_number,
            "cardholder_name": self.cardholder_name,
            "expiration_date": self.expiration_date,
            "active": self.active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

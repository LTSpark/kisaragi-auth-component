from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import EmbeddedDocument, StringField, DateTimeField, ObjectIdField, BooleanField, DateField


class Address(EmbeddedDocument):

    _id = ObjectIdField(required=True, default=ObjectId)

    address = StringField(required=True)
    district = StringField(required=True)
    city = StringField(required=True)
    zipcode = StringField(require=True)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    def to_dict(self):
        return {
            "address_id": str(self._id),
            "address": self.address,
            "district": self.district,
            "city": self.city,
            "zipcode": self.zipcode,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
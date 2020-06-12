from marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "date_created", "_links")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
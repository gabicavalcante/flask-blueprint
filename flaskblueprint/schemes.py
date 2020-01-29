from marshmallow import Schema, fields


class UserAPISchema(Schema):
    id = fields.Str(required=True)
    username = fields.Str(required=True)
    created_at = fields.DateTime()


class CreateUserAPISchema(UserAPISchema):
    password = fields.Str(required=True)

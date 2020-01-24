from marshmallow import Schema, fields


class TaskAPISchema(Schema):
    description = fields.Str(required=True)
    script = fields.Str(required=True)


class TaskResposeSchema(TaskAPISchema):
    id = fields.Str(required=True)
    created_at = fields.DateTime()

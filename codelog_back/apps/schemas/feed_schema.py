from marshmallow import Schema, fields


class GetFeedListResponseSchema(Schema):
    id = fields.Integer(required=True)
    nickname = fields.String(required=True)
    image = fields.String(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    url = fields.String(required=True)
    tags = fields.List(fields.Str)
    created_at = fields.String()
    updated_at = fields.String()


class CreateFeedRequestSchema(Schema):
    url = fields.String(required=True)
    tags = fields.String(required=True)


class CreateFeedResponseSchema(Schema):
    id = fields.Integer(required=True)
    nickname = fields.String(required=True)
    image = fields.String(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    url = fields.String(required=True)
    tags = fields.List(fields.Str)
    created_at = fields.String()
    updated_at = fields.String()

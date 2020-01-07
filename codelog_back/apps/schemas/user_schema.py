from marshmallow import Schema, fields


class OAuthLoginResponseSchema(Schema):
    token = fields.String(required=True)
    refresh_token = fields.String(required=True)

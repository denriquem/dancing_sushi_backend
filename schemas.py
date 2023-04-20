from marshmallow import Schema, fields


class ImageSchema(Schema):
    id = fields.Str(dump_only=True)
    userId = fields.Str(dump_only=True)
    image_url = fields.Str(required=True)
    image_title = fields.Str(required=True)


class ImageUpdateSchema(Schema):
    image_title = fields.Str(required=True)

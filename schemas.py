from marshmallow import Schema, fields


class ImageSchema(Schema):
    image_id = fields.Int(dump_only=True)
    userId = fields.Int(required=True, load_only=True)
    image_url = fields.Str(required=True)
    image_title = fields.Str(required=True)


class ImageUpdateSchema(Schema):
    image_title = fields.Str(required=True)

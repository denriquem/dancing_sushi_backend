from marshmallow import Schema, fields


class ImageSchema(Schema):
    image_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, load_only=True)
    image_url = fields.Str(required=True)
    image_title = fields.Str(required=True)


class ImageUpdateSchema(Schema):
    image_title = fields.Str(required=True)
    user_id = fields.Int()


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    user_email = fields.Str(required=True)
    password = fields.Str(required=True)

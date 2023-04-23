import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schemas import ImageSchema, ImageUpdateSchema
from models import ImageModel
from db import db

blp = Blueprint('images', " __name__", description="operations on images")


@blp.route('/image/<string:image_id>')
class Image(MethodView):
    @blp.response(200, ImageSchema)
    def get(self, image_id):
        try:
            return images[image_id]
        except KeyError:
            abort(404, message="image not found")

    def delete(self, image_id):
        try:
            del images[image_id]
        except KeyError:
            abort(404, message="image not found")

    @blp.arguments(ImageUpdateSchema)
    @blp.response(200, ImageSchema)
    def put(self, image_data, image_id):
        if "image_url" not in image_data:
            abort(400, message="image_url not in update request")
        try:
            image = images[image_id]
            image |= image_data
            return image
        except:
            abort(404, message="image not found")


@blp.route('/images')
class Image(MethodView):
    def get(self):
        return {"test": 'bla'}

    @blp.arguments(ImageSchema)
    @blp.response(200, ImageSchema)
    def post(self, request_data):
        image = ImageModel(**request_data)
        
        try:
            db.session.add(image)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item")

        return image, 201

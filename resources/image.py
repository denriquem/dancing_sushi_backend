import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schemas import ImageSchema, ImageUpdateSchema
from models import ImageModel
from db import db

blp = Blueprint('images', " __name__", description="operations on images")


@blp.route('/images/<string:image_id>')
class Image(MethodView):
    @blp.response(200, ImageSchema)
    def get(self, image_id):
        image = ImageModel.query.get_or_404(image_id)
        return image

    def delete(self, image_id):
        image = ImageModel.query.get_or_404(image_id)
        raise NotImplementedError("Deleting an image is not implemented")

    @blp.arguments(ImageUpdateSchema)
    @blp.response(200, ImageSchema)
    def put(self, image_data, image_id):
        image = ImageModel.query.get_or_404(image_id)
        raise NotImplementedError("Updating an image is not implemented")


@blp.route('/images')
class Image(MethodView):
    def get(self):
        print("helooo????")
        return {"test": 'bla'}

    @blp.arguments(ImageSchema)
    @blp.response(200, ImageSchema)
    def post(self, request_data):
        image = ImageModel(**request_data)
        
        print(image)

        try:
            db.session.add(image)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item")

        return image, 201

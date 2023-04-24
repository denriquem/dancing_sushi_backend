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
        db.session.delete(image)
        db.session.commit()
        return {"message": "Image deleted"}

    @blp.arguments(ImageUpdateSchema)
    @blp.response(200, ImageSchema)
    def put(self, image_data, image_id):
        image = ImageModel.query.get(image_id)
        if image:
            image.image_url = image_data["image_url"]
            image.image_title = image_data["image_title"]
        else:
            image = ImageModel(id=image_id, **image_data)
        db.session.add(image)
        db.session.commit()
        return image


@blp.route('/images')
class Image(MethodView):
    @blp.response(200, ImageSchema(many=True))
    def get(self):
        return ImageModel.query.all()

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

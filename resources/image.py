import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import images

blp = Blueprint("images", " __name__", description="operations on images")


@blp.route('/image/<string:image_id>')
class Image(MethodView):
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

    def put(self, image_id):
        image_data = request.get_json()
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
        return images

    def createImage(self):
        request_data = request.get_json()
        image_id = uuid.uuid4.hex()
        newImage = {**request_data, id: image_id}
        images[image_id] = newImage
        return newImage, 201

# @blp.route("/comments/<string:image_id>")
# class Comment(MethodView):
#     def getCommentForImage(self, image_id):
#         filtered_comments = []
#         for comment in comments:
#             if comment["image_id"] == image_id:
#                 filtered_comments.append(comment)
#         return filtered_comments

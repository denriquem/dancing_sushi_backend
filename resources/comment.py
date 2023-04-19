from flask.views import MethodView
from flask_smorest import Blueprint
from db import comments

blp = Blueprint("images", " __name__", description="operations on images")


@blp.route("/comments/<string:image_id>")
class Comment(MethodView):
    def get(self, image_id):
        filtered_comments = []
        for comment in comments:
            if comment["image_id"] == image_id:
                filtered_comments.append(comment)
        return filtered_comments

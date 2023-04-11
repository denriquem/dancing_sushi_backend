import uuid
from flask import Flask, request
from flask_smorest import abort
from db import comments, reactions, images

app = Flask(__name__)


@app.get("/images")
def get_images():
    return images


@app.get("/images/<string:image_id>")
def get_image_by_id(image_id):
    try:
        return images[image_id]
    except KeyError:
        abort(404, message="image not found")


@app.post("/image")
def create_image():
    request_data = request.get_json()
    image_id = uuid.uuid4.hex()
    newImage = {**request_data, id: image_id}
    images[image_id] = newImage
    return newImage, 201


@app.delete("/images/<string:image_id")
def delete_image(image_id):
    try:
        del images[image_id]
    except KeyError:
        abort(404, message="image not found")


@app.put("/images/<string:image_id")
def update_image(image_id):
    image_data = request.get_json()
    if "image_url" not in image_data:
        abort(400, message="image_url not in update request")
    try:
        image = images[image_id]
        image |= image_data
        return image
    except:
        abort(404, message="image not found")


@app.get("/comments/<string:image_id>")
def get_comments_for_image(image_id):
    filtered_comments = []
    for comment in comments:
        if comment["image_id"] == image_id:
            filtered_comments.append(comment)
    return filtered_comments

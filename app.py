import uuid
from flask import Flask, request
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
        return {"message": "store not found"}, 404


@app.post("/image")
def create_image():
    request_data = request.get_json()
    image_id = uuid.uuid4.hex()
    newImage = {**request_data, id: image_id}
    images[image_id] = newImage
    return newImage, 201


@app.get("/comments/<string:image_id>")
def get_comments_for_image(image_id):
    filtered_comments = []
    for comment in comments:
        if comment["image_id"] == image_id:
            filtered_comments.append(comment)
    return filtered_comments

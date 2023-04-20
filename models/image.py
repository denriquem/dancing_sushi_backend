from db import db


class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primaryKey=True)
    image_url = db.Column(db.String(80), unique=True, nullable=False)
    image_title = db.Column(db.String(80), unique=False)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)
    # user = db.relationship("UserModel", back_populates="images")

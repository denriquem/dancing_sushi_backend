from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primaryKey=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    # images = db.relationship("ImageModel", back_poppulates="user", lazy="dynamic")

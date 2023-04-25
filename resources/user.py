from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from models import UserModel
from db import db

from passlib.hash import pbkdf2_sha256

blp = Blueprint('users', " __name__", description="operations on users")


@blp.route('/register')
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists")

        user = UserModel(
            username=user_data["username"],
            pasword=pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created succesfully"}, 201


@blp.route('/user/<int:user_id>')
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit(user)
        return {"Message": "User Deleted"}, 200

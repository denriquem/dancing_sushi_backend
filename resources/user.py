from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema
from models import UserModel
from db import db

from flask_jwt_extended import create_access_token
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
            user_email=user_data["user_email"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created succesfully"}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.user_id)
            return {"access_token": access_token}

        abort(401, message="invalide credentials")


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

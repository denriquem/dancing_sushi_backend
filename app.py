import secrets
from flask import Flask
from flask_smorest import Api
from resources.image import blp as ImageBlueprint
from resources.user import blp as UserBlueprint
from db import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()


def createApp(db_url=None):
    app = Flask(__name__)

    app.config["API_TITLE"] = "Images REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCEHMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_STRING")

    db.init_app(app)

    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ImageBlueprint)
    api.register_blueprint(UserBlueprint)

    return app


app = createApp()

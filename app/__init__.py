from flask import Flask
from . import routes
from .database import User, db , Prediction, bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(routes.bp)

    return app

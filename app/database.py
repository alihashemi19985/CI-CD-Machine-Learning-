from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(100), nullable = False, unique=True)
    email = db.Column(db.String(100), nullable = False, unique=True)
    predictions = db.relationship('Prediction', backref='users', lazy=True)


class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    Pclass = db.Column(db.Integer, nullable=False)
    sex=db.Column(db.String, nullable=False)
    age=db.Column(db.Integer, nullable=False)
    embarked =db.Column(db.String, nullable=False)
    prediction_result = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default= datetime.now(timezone.utc))


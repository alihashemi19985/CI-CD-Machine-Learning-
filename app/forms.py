from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired('Username cannot be empty'), Length(min=6, message = "Username should be at least 6 characters long") ])
    email = StringField('Email', [DataRequired("Email cannot be empty"), Email(message ="Invalid email address")])
    password = PasswordField('Password', [DataRequired('Password cannot be empty'), Length(min=8, message = "Password must be at least 8 characters long") ])
    confirm_password = PasswordField('Confirm Password', [DataRequired('This filed cannot be empty'), EqualTo('password', message="Passwords must match each other") ])
    register = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired('Username cannot be empty') ])
    password = PasswordField('Password', [DataRequired('Password cannot be empty')])
    login = SubmitField('Login')

class InputForm(FlaskForm):
    Pclass = IntegerField(label ='Pclass', validators=[DataRequired('This feature cannot be empty')])
    sex = StringField(label ='Sex', validators=[DataRequired('This feature cannot be empty')])
    age = IntegerField(label ='Age', validators=[DataRequired('This feature cannot be empty') ])
    embarked = StringField(label ='Embarked', validators=[DataRequired('This feature cannot be empty')])
    predict = SubmitField('Predict')
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    Blueprint,
    session,
    request,
)
import numpy as np 
from flask_bcrypt import Bcrypt
from .database import User, db, Prediction, bcrypt
from .forms import RegistrationForm, LoginForm, InputForm
from  .model.model import prediction_model

bp = Blueprint("main", __name__)
# bcrypt = Bcrypt()


@bp.route("/")
def home():
    return render_template("home.html")


@bp.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("You already have an account. Please log in.", "warning")
            return redirect(url_for("main.login"))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf8')
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Register Successfull')
        return redirect(url_for('main.login'))
    return render_template("register.html", form = form)

@bp.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_check = User.query.filter_by(username=username).first()
        if user_check is None:
            flash("This username is not registered. Please Register.", "warning")
            return redirect(url_for("main.login"))
        if user_check and bcrypt.check_password_hash(user_check.password, password):
            session['username'] = username
            flash("Login successful!", "success")
            return redirect(url_for('main.input_data'))
        else:
            flash("Login failed. Please check your username and password.", "danger")
            return redirect(url_for("main.login"))
    return render_template("login.html", form=form)

def login_required(f):
    def wrap(*args, **kwargs):
        if "username" not in session:
            flash("You need to login first!", "danger")
            return redirect(url_for("main.login"))
        return f(*args, **kwargs)

    wrap.__name__ = f.__name__
    return wrap


@bp.route("/input", methods=["GET", "POST"])
@login_required
def input_data():
    form=InputForm()

    if request.method == 'POST':
        sex = request.form.get("sex")
        age = request.form.get("age")
        pclass = request.form.get("pclass")
        embarked = request.form.get("embarked")

        if not sex or not age or not pclass or not embarked:
            flash("Missing data! Please fill out all fields.", "warning")
            return render_template("error.html",error = 400), 400  # Return custom error page with 400 status code
        
        features = [
            float(request.form['pclass']),
            request.form['sex'],
            float(request.form['age']),
            request.form['embarked']
        ]

        predicted_class = prediction_model(features)  ##machine learning model
        predict_result = 'Survived' if predicted_class == 1 else 'Not Survived'

        user_check = User.query.filter_by(username =session['username']).first()
        new_input = Prediction(
            user_id= user_check.id,
            Pclass = pclass,
            sex= sex,
            age= age,
            embarked = embarked,
            prediction_result = predict_result
        )
        db.session.add(new_input)
        db.session.commit()
        return render_template("result.html" , predicted_class = predicted_class)
       
    return render_template("input.html", form = form)

@bp.route("/history", methods=["GET"])
@login_required
def history():
    current_user = User.query.filter_by(username=session["username"]).first()
    predictions = Prediction.query.filter_by(user_id=current_user.id).all()
    # print(predictions[1].sex)
    return render_template("history.html", predictions=predictions)

@bp.route("/profile", methods=["GET"])
@login_required
def profile():
    current_user = User.query.filter_by(username=session["username"]).first()
    # predictions = Prediction.query.filter_by(user_id=current_user.id).all()
    # print(current_user.email)
    return render_template("profile.html", user_info=current_user)
    

@bp.route("/error", methods=["GET"])
def error():

    return render_template("error.html",error=500)


@bp.app_errorhandler(401)
def unauthorized_error(e):
    flash("You need to be logged in to access this page.", "warning")
    # return redirect(url_for("main.login"))
    return render_template("error.html",error=401), 401


@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("error.html",error=404), 404

@bp.app_errorhandler(500)
def internal_server_error(e):
    # Log the error details (optional, for debugging)
    # app.logger.error(f"Server Error: {e}")
    return render_template("error.html",error=500), 500



@bp.route("/logout")
def logout():
    session.pop("username",None)
    session.clear()
    flash("You are logged out", "success")

    return redirect(url_for("main.home"))

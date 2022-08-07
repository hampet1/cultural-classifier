from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                # remember use
                login_user(user, remember=True)
                flash("You have successfully logged in", category="success")
                return redirect(url_for('maps.map'))
            else:
                flash("You entered wrong password", category="error")
        else:
            flash("User does not exist", category="error")


    return render_template("public/login.html" , user = current_user, page="log_in")


@auth.route("/logout")
@login_required
def log_out():
    logout_user()
    flash("you were successfully logged out", category="success")
    return redirect(url_for('views.home'))


@auth.route("/sign-up", methods=['POST','GET'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('confirm-password')

        # check if email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash("user already exist", category="error")
        elif len(first_name) < 2:
            flash("Your first name must be longer then one character", category="error")
        elif len(last_name) < 2:
            flash("Your last name must be longer then one character", category="error")
        elif len(email) < 3:
            flash("Your email address is too short", category="error")
        elif len(password) < 6:
            flash("Your password must be at least 6 characters", category="error")
        elif password != password_confirm:
            flash("Passwords do not match", category="error")
        else:
            new_user = User(first_name=first_name,last_name=last_name, email=email, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #log in user after signing up
            login_user(new_user, remember=True)
            flash("User Account has been created", category="success")
            # after sign up redirect user to hom page
            return redirect(url_for('views.home'))

    return render_template("public/signup.html", user=current_user, page="sign_up")

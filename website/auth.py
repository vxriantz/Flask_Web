from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db


auth = Blueprint('auth', __name__)
# Signup route
@auth.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        # Requesting certain elements from database
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

# Looking through database to find if email is taken / which email was first
        user = User.query.filter_by(email=email).first()
        # Creates and flashs error message if email already found
        if user:
            flash('Email Already Exists.', category='error')
        # Email cannot be shorter than 4 characters long, error message
        elif len(email) < 4:
            flash('Email is not valid.', category='error')
        # Username cannot be shorter than 3 characters long
        elif len(username) < 3:
            flash('Username must be at least 3 characters.', category='error')
        # Passwords must match, overwise error message
        elif password1 != password2: 
            flash('Passwords do not match.', category='error')
        # Password cannot be shorter than 8 charatcers, otherwise error message
        elif len(password1) < 8:
            flash('Password must have at least 8 characters.', category='error')
        else:
            #If everything dosent result in error, the new information is commited to the database
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='scrypt:32768:8:1'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created.', category='success')
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user = current_user)


# Login route
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('You have logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password.', category='error')
        else:
             flash('Email does not exist!', category='error')
    return render_template('login.html', user=current_user)


# logout route
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
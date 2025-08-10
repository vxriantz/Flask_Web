from flask import Blueprint, render_template


# set blueprint
views = Blueprint("views", __name__)


# default / home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html")


# gallery route
@views.route("/gallery")
def gallery():
    return render_template("gallery.html")


# contact route
@views.route("/contact")
def contact():
    return render_template("contact.html")

# sign up route
@views.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")
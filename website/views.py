from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# set blueprint
views = Blueprint("views", __name__)


# default / home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html")


# about route
@views.route("/about")
def about():
    return render_template("about.html")

# cookie type route
@views.route("/cookie_type")
def cookie_type():
    return render_template("cookie_type.html")

# cookies route
@views.route("/cookies")
def cookies():
    return render_template("cookies.html")

# sign up route
@views.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

# login route
@views.route("/sign_up")
def login():
    return render_template("login.html")

# faq route
#faq route
@views.route("/faq", methods=['POST', 'GET'])
def faq():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) <1:
            flash('Comment cannot be empty.')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment Added.', category='success')
    
    return render_template("faq.html", user=current_user)

# gingerbrave route
@views.route("/gingerbrave")
def gingerbrave():
    return render_template("gingerbrave.html")

# strawberry cookie route
@views.route("/strawberry")
def strawberry():
    return render_template("strawberry.html")

# wizard cookie route
@views.route("/wizard")
def wizard():
    return render_template("wizard.html")

# custard cookie iii route
@views.route("/custard")
def custard():
    return render_template("custard.html")

# chili pepper cookie route
@views.route("/chili")
def chili():
    return render_template("chili.html")

# lime cookie route
@views.route("/lime")
def lime():
    return render_template("lime.html")

# jagae cookie route
@views.route("/jagae")
def jagae():
    return render_template("jagae.html")

# manju cookie route
@views.route("/manju")
def manju():
    return render_template("manju.html")
from flask import Blueprint, render_template


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


# combat type route
@views.route("/combat_type")
def combat_type():
    return render_template("combat_type.html")

# sign up route
@views.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

# faq route
@views.route("/faq")
def faq():
    return render_template("faq.html")

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
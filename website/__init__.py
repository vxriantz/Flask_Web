# import external libraries

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# create app function
# returns app

def create_app():
    app = Flask(__name__)

    # import views from views.py
    from .views import views

    # register blueprints
    app.register_blueprint(views, url_prefix ="/")

    return app
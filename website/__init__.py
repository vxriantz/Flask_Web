# import external libraries

from flask import Flask, send_from_directory
#pip install Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user


db = SQLAlchemy()
DB_NAME = "database.db"

# create app function
# returns app

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cookies'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
#Import views from views.py
    from .views import views
    from .auth import auth

    #Register blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    


    return app
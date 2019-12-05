from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from environs import Env

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    env_name = env('FLASK_ENV', 'Development')
    app.config.from_object(config[env_name])
    config[env_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main_bp as main_blueprint
    from .main.endpoints.users import users

    app.register_blueprint(main_blueprint)
    app.register_blueprint(users.users_bp)

    return app

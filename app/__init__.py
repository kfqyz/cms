from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
mail = Mail()
babel = Babel()
moment = Moment()
db = SQLAlchemy()
admin = Admin()

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    babel.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .admin_views import add_admin_views

    add_admin_views()

    return app

from flask import Flask
# from flask_admin import Admin
from flask_avatars import Avatars
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee

from config import config

bootstrap = Bootstrap()
mail = Mail()
babel = Babel()
moment = Moment()
db = SQLAlchemy()
# admin = Admin()
ckeditor = CKEditor()
avatars = Avatars()
whooshee = Whooshee()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = '请登录后访问'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    babel.init_app(app)
    # admin.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    avatars.init_app(app)
    whooshee.init_app(app)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # from .admin_views import add_admin_views

    # add_admin_views()

    return app

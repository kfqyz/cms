from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config
from . import admin

bootstrap = Bootstrap()
mail = Mail()
babel = Babel()
moment = Moment()
db = SQLAlchemy()


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
    login_manager.init_app(app)

    from .blog import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    admin = Admin(app=app, name='后台管理', template_mode='bootstrap3')
    from flask_admin.contrib.sqla import ModelView
    from .models import User, Role, Post, Comment, Follow

    @babel.localeselector
    def get_locale():
        from flask import session
        return session.get('lang', 'zh_CN')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(Follow, db.session))

    return app

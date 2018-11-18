from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
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

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 后台管理模块
    admin = Admin(app, '后台管理', index_view=AdminIndexView(), template_mode='bootstrap3')

    from app.models import User, Role, Post, Comment, Follow

    class UserView(ModelView):
        can_delete = False
        column_exclude_list = ['password_hash', 'about_me']
        column_searchable_list = ['username', 'email']

    admin.add_view(UserView(User, db.session, name='用户'))
    admin.add_view(ModelView(Role, db.session, name='角色'))
    admin.add_view(ModelView(Post, db.session, name='文章'))
    admin.add_view(ModelView(Comment, db.session, name='评论'))
    admin.add_view(ModelView(Follow, db.session, name='关注'))

    # 后台中文化
    @babel.localeselector
    def get_locale():
        from flask import session
        return session.get('lang', 'zh_CN')

    return app

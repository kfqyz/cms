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

    from .models import User, Role, Post, Category, Tag, Comment, Follow

    class UserView(ModelView):
        can_delete = False
        column_exclude_list = ['password_hash', 'about_me', 'posts', 'followers', 'followed']
        column_searchable_list = ['username', 'email']
        column_labels = dict(username='用户名', email='邮箱', phone_number='电话', role='角色', confirmed='验证', name='姓名',
                             location='地址', memeber_sence='注册时间', last_seen='最后登录')

    admin.add_view(UserView(User, db.session, name='用户'))
    admin.add_view(ModelView(Role, db.session, name='角色'))
    admin.add_view(ModelView(Post, db.session, name='文章'))
    admin.add_view(ModelView(Category, db.session, name='分类'))
    admin.add_view(ModelView(Tag, db.session, name='标签'))
    admin.add_view(ModelView(Comment, db.session, name='评论'))
    admin.add_view(ModelView(Follow, db.session, name='关注'))

    # 后台中文化
    @babel.localeselector
    def get_locale():
        from flask import session
        return session.get('lang', 'zh_CN')

    return app

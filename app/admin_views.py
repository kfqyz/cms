from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from . import admin, db, babel
from .models import User, Role, Post, Category, Tag, Comment, Follow


def add_admin_views():
    # 后台管理模块
    admin.name = '后台管理'
    admin.index_view = AdminIndexView()
    admin.template_mode = 'bootstrap3'

    class UserView(ModelView):
        can_edit = False
        column_exclude_list = ['password_hash', 'about_me', 'posts', 'followers', 'followed']
        column_searchable_list = ['username', 'email', 'phone_number', 'location', 'name']
        column_editable_list = ['username', 'email', 'phone_number', 'role', 'confirmed', 'name', 'location']
        column_labels = dict(username='用户名', email='邮箱', phone_number='电话', role='角色', confirmed='验证', name='姓名',
                             location='地址', member_since='注册时间', last_seen='最后登录')

        def is_accessible(self):
            return current_user.is_administrator()

    class RoleView(ModelView):
        column_editable_list = ['name', 'default', 'permissions']
        column_labels = dict(name='角色名称', default='缺省角色', permissions='权限')

        def is_accessible(self):
            return current_user.is_administrator()

    class PostView(ModelView):
        column_searchable_list = ['title', 'body', 'author_id']
        column_editable_list = ['title', 'body']
        column_labels = dict(title='标题', body='内容', author='作者', timestamp='发布时间')

        def is_accessible(self):
            return current_user.is_administrator()

    class CategoryView(ModelView):
        column_searchable_list = ['name']
        column_editable_list = ['name', 'user']
        column_labels = dict(name='类别名称', user='所属用户')

        def is_accessible(self):
            return current_user.is_administrator()

    class TagView(ModelView):
        column_searchable_list = ['name']
        column_editable_list = ['name']
        column_labels = dict(name='标签名')

        def is_accessible(self):
            return current_user.is_administrator()

    class CommentView(ModelView):
        column_searchable_list = ['body', 'author_id', 'post_id', 'disabled', 'timestamp']
        column_editable_list = ['body', 'disabled']
        column_labels = dict(body='内容', author='发表者', post='评论文章', disabled='禁止否', timestamp='时间')

        def is_accessible(self):
            return current_user.is_administrator()

    class FollowView(ModelView):
        column_searchable_list = ['follower_id', 'followed_id']
        column_labels = dict(follower='关注者', followed='被关注', timestamp='关注时间')

        def is_accessible(self):
            return current_user.is_administrator()

    admin.add_view(UserView(User, db.session, name='用户'))
    admin.add_view(RoleView(Role, db.session, name='角色'))
    admin.add_view(PostView(Post, db.session, name='文章'))
    admin.add_view(CategoryView(Category, db.session, name='分类'))
    admin.add_view(TagView(Tag, db.session, name='标签'))
    admin.add_view(CommentView(Comment, db.session, name='评论'))
    admin.add_view(FollowView(Follow, db.session, name='关注'))

    # 后台静态文件管理
    import os.path as op
    from flask_admin.contrib.fileadmin import FileAdmin
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name='静态文件'))

    # 后台中文化
    @babel.localeselector
    def get_locale():
        from flask import session
        return session.get('lang', 'zh_CN')
import os

from flask import render_template, redirect, url_for, flash, request, current_app, abort, make_response, \
    send_from_directory
from flask_ckeditor import upload_fail, upload_success
from flask_login import login_required, current_user

from app import db
from app.models.category import Category
from app.models.comment import Comment
from app.models.post import Post
from app.models.role import Role, Permission
from app.models.tag import Tag
from app.models.user import User
from . import blog
from .forms import EditProfileForm, EditProfileAdminForm, PostForm, CommentForm
from ..decorators import admin_required, permission_required


@blog.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    show_followed = False
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed', ''))
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query
    pagination = query.order_by(Post.create_time.desc()).paginate(page,
                                                                  per_page=current_app.config['CMS_POSTS_PER_PAGE'],
                                                                  error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, show_followed=show_followed, pagination=pagination)


# 文章列表
@blog.route('/post_list')
def post_list():
    tag = Tag.query.filter_by(name=request.args.get('tag')).first()
    category = Category.query.filter_by(name=request.args.get('category')).first()
    page = request.args.get('page', 1, type=int)
    if tag or category:
        pagination = Post.query.with_parent(category or tag).order_by(Post.create_time.desc()).paginate(page,
                                                                                                        per_page=
                                                                                                        current_app.config[
                                                                                                            'CMS_POSTS_PER_PAGE'],
                                                                                                        error_out=False)
        posts = pagination.items
        return render_template('blog/post_list.html', category=category, tag=tag, posts=posts, pagination=pagination)
    else:
        pagination = Post.query.order_by(Post.create_time.desc()).paginate(page,
                                                                           per_page=
                                                                           current_app.config[
                                                                               'CMS_POSTS_PER_PAGE'],
                                                                           error_out=False)
        posts = pagination.items
        return render_template('blog/post_list.html', posts=posts, pagination=pagination)


# 用户页面
@blog.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, int)
    pagination = user.posts.order_by(Post.create_time.desc()).paginate(page,
                                                                       per_page=current_app.config[
                                                                           'CMS_POSTS_PER_PAGE'],
                                                                       error_out=False)
    posts = pagination.items
    return render_template('blog/user.html', user=user, posts=posts, pagination=pagination)


# 修改个人资料
@blog.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone_number = form.phone_number.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('你已经成功更新个人资料。')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.phone_number.data = current_user.phone_number
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('blog/edit_profile.html', form=form)


@blog.route('/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)


# 管理员修改用户资料
@blog.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.phone_number = form.phone_number.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('你已经成功更新个人资料。')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.phone_number.data = user.phone_number
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('blog/edit_profile.html', form=form, user=user)


# 文章详情--发评论页面
@blog.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        if form.replied_id.data:
            comment = Comment(body=form.body.data, replied_id=form.replied_id.data,
                              author=current_user._get_current_object())
        else:
            comment = Comment(body=form.body.data, post=post, author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash('成功发表评论')
        return redirect(url_for('.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // current_app.config['CMS_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.filter(Comment.disabled != True).order_by(Comment.create_time.desc()).paginate(page,
                                                                                                              per_page=
                                                                                                              current_app.config[
        'CMS_COMMENTS_PER_PAGE'], error_out=False)
    comments = pagination.items
    return render_template('blog/post.html', post=post, form=form, comments=comments, pagination=pagination)


# 修改文章
@blog.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and not current_user.can(Permission.ADMIN):
        abort(403)
    form = PostForm(post=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.categorys = [Category.query.filter_by(id=id).first() for id in form.categorys.data]
        post.body = form.body.data

        for name in form.tags.data.split():
            tag = Tag.query.filter_by(name=name).first()
            if tag is None:
                tag = Tag(name=name)
                db.session.add(tag)
            if tag not in post.tags:
                post.tags.append(tag)

        for tag in post.tags:
            if tag.name not in form.tags.data.split():
                db.session.delete(tag)

        db.session.add(post)
        db.session.commit()
        flash('文章修改成功！')
        return redirect(url_for('.post', id=post.id))
    form.title.data = post.title
    form.categorys.data = [category.id for category in post.categorys.all()]
    form.tags.data = ' '.join([tag.name for tag in post.tags.all()])
    form.body.data = post.body
    return render_template('blog/edit_post.html', form=form)


# 新建文章
@blog.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data,
                    categorys=[Category.query.filter_by(id=id).first() for id in form.categorys.data],
                    author=current_user._get_current_object())

        for name in form.tags.data.split():
            tag = Tag.query.filter_by(name=name).first()
            if tag is None:
                tag = Tag(name=name)
                db.session.add(tag)
            post.tags.append(tag)

        db.session.add(post)
        db.session.commit()
        flash('文章发表成功！')
        return redirect(url_for('.post', id=post.id))
    return render_template('blog/new_post.html', form=form)


# 删除文章
@blog.route('/delete_post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('要删除的文章不存在。')
        return redirect(url_for('.index'))
    user = User.query.filter_by(id=post.author_id).first()
    if current_user.id == user.id or current_user.is_administrator():
        db.session.delete(post)
        db.session.commit()
        flash('文章删除成功。')
        return redirect(url_for('.index'))
    flash('你没删除的权限')
    return redirect(url_for('.index'))


# 关注用户
@blog.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('没有此用户')
        return redirect(url_for('.index'))
    if current_user.is_following(user):
        flash('你已经关注此用户了')
        return redirect(url_for('.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('你成功关注了{}'.format(username))
    return redirect(url_for('.user', username=username))


# 我的粉丝页面
@blog.route('/followers/<username>')
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('没有此用户')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, int)
    pagination = user.followers.paginate(page, per_page=current_app.config['CMS_FOLLOWERS_PER_PAGE'], error_out=False)
    follows = [{'user': item.follower, 'create_time': item.create_time} for item in pagination.items]
    return render_template('blog/followers.html', user=user, title='Followers of', endpoint='.followers',
                           pagination=pagination, follows=follows)


# 取消关注
@blog.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('没有此用户')
        return redirect(url_for('.index'))
    if not current_user.is_following(user):
        flash('你没有关注此用户')
        return redirect(url_for('.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('你已经取消关注{}'.format(username))
    return redirect(url_for('.user', username=username))


# 某用户的粉丝
@blog.route('/followed_by/<username>')
def followed_by(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('没有此用户')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followed.paginate(
        page, per_page=current_app.config['CMS_FOLLOWERS_PER_PAGE'],
        error_out=False)
    follows = [{'user': item.followed, 'create_time': item.create_time}
               for item in pagination.items]
    return render_template('blog/followers.html', user=user, title="{}关注的用户".format(user.username),
                           endpoint='.followed_by', pagination=pagination,
                           follows=follows)


# 首页tab:显示所有最新文章
@blog.route('/all')
@login_required
def show_all():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '', max_age=30 * 24 * 60 * 60)
    return resp


# 首页tab:显示关注的最新文章
@blog.route('/followed')
@login_required
def show_followed():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '1', max_age=30 * 24 * 60 * 60)
    return resp


# # 管理评论
# @blog.route('/moderate')
# @login_required
# @permission_required(Permission.MODERATE)
# def moderate():
#     page = request.args.get('page', 1, int)
#     pagination = Comment.query.order_by(Comment.create_time.desc()).paginate(page, per_page=current_app.config[
#         'CMS_COMMENTS_PER_PAGE'], error_out=False)
#     comments = pagination.items
#     return render_template('blog/moderate.html', comments=comments, pagination=pagination, page=page)
#
#
# # 取消禁止评论
# @blog.route('/moderate/enable/<int:id>')
# @login_required
# @permission_required(Permission.MODERATE)
# def moderate_enable(id):
#     comment = Comment.query.get_or_404(id)
#     comment.disabled = False
#     db.session.add(comment)
#     db.session.commit()
#     return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))
#
#
# # 禁止评论
# @blog.route('/moderate/disable/<int:id>')
# @login_required
# @permission_required(Permission.MODERATE)
# def moderate_disable(id):
#     comment = Comment.query.get_or_404(id)
#     comment.disabled = True
#     db.session.add(comment)
#     db.session.commit()
#     return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))


# 文章分类列表
@blog.route('/category/<int:c_id>')
def category_post(c_id=1):
    page = request.args.get('page', 1, type=int)
    category = Category.query.get_or_404(c_id)
    # pagination = category.posts.order_by(Post.create_time.desc()).paginate(page, per_page=current_app.config[
    #     'CMS_POSTS_PER_PAGE'], error_out=False)
    pagination = Post.query.with_parent(category).order_by(Post.create_time.desc()).paginate(page, per_page=
    current_app.config[
        'CMS_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    return render_template('blog/category_post.html', category=category, posts=posts, pagination=pagination)


@blog.route('/files/<filename>')
def uploaded_files(filename):
    path = current_app.config['BLOG_PIC_PATH']
    return send_from_directory(path, filename)


@blog.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='只能上传图片文件！')
    f.save(os.path.join(current_app.config['BLOG_PIC_PATH'], f.filename))
    url = url_for('.uploaded_files', filename=f.filename)
    return upload_success(url=url)

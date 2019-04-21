from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.auth import auth
from app.email import send_email
from app.models.user import User
from .forms import LoginForm, RegistrationForm, ChangeEmailForm, PasswordResetForm, PasswordResetRequestForm, \
    ChangePasswordForm


# 记录用户访问时间并检查用户是否通过验证
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


# 未验证用户
@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('blog.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.account.data).first() \
               or User.query.filter_by(email=form.account.data).first() \
               or User.query.filter_by(phone_number=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('blog.index')
            return redirect(next)
        flash('输入的用户名或密码不正确！')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录！')
    return redirect(url_for('blog.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, phone_number=form.phone_number.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '验证你的账号', 'auth/email/confirm', user=user, token=token)
        flash('验证邮件已经发到你的邮箱。')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('blog.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('你已经成功验证账号，谢谢！')
    else:
        flash('验证账号无效或已经过期！')
    return redirect(url_for('blog.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '账号验证',
               'auth/email/confirm', user=current_user, token=token)
    flash('新的验证邮件已经发到你的邮箱，请查收。')
    return redirect(url_for('blog.index'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('密码修改成功')
            return redirect(url_for('blog.index'))
        else:
            flash('密码修改失败')
    return render_template("auth/change_password.html", form=form)


@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('blog.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, '重置你的密码',
                       'auth/email/reset_password',
                       user=user, token=token)
        flash('重置密码的链接已经发到你的注册邮箱，请登录邮箱，点击链接修改密码。')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('blog.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        if User.reset_password(token, form.password.data):
            db.session.commit()
            flash('密码重置成功，请用新密码登录。')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('blog.index'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, '验证你的邮箱',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('邮件已经发到你的新邮箱，请登录邮箱，点击链接进行验证。')
            return redirect(url_for('blog.index'))
        else:
            flash('无效的邮箱或密码')
    return render_template("auth/change_email.html", form=form)


@auth.route('/change_email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        db.session.commit()
        flash('邮箱修改成功')
    else:
        flash('无效的请求')
    return redirect(url_for('blog.index'))

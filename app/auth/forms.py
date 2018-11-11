from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

from ..models import User


class LoginForm(FlaskForm):
    account = StringField('用户名/邮箱/手机号', validators=[DataRequired(), Length(1, 64)], render_kw={'placeholder': '用户名/邮箱/手机号'})
    password = PasswordField('密  码', validators=[DataRequired()], render_kw={'placeholder': '请输入密码'})
    remember_me = BooleanField('下次自动登录')
    submit = SubmitField('登  录')


class RegistrationForm(FlaskForm):
    email = StringField('邮  箱', validators=[DataRequired(), Length(1, 64), Email()], render_kw={'placeholder': '请输入邮箱'})
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64), \
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                     '用户名只能由字母、数字、点或下划线组成！')], render_kw={'placeholder': '请输入用户名'})
    password = PasswordField('密  码', validators=[DataRequired()], render_kw={'placeholder': '请输入密码'})
    password2 = PasswordField('重复密码', validators=[DataRequired(), \
                                                  EqualTo('password', message='重复密码不一致')], render_kw={'placeholder': '请再次输入密码'})
    submit = SubmitField('注  册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经注册了！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经存在！')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, NumberRange

from ..models import User


# 登录表单
class LoginForm(FlaskForm):
    account = StringField('用户名/邮箱/手机号', validators=[DataRequired(), Length(1, 64)],
                          render_kw={'placeholder': '用户名/邮箱/手机号'})
    password = PasswordField('密  码', validators=[DataRequired()], render_kw={'placeholder': '请输入密码'})
    remember_me = BooleanField('下次自动登录')
    submit = SubmitField('登  录')


# 注册表单
class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64), \
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                     '用户名只能由字母、数字、点或下划线组成！')], render_kw={'placeholder': '请输入用户名'})
    email = StringField('邮  箱', validators=[DataRequired(), Length(1, 64), Email()], render_kw={'placeholder': '请输入邮箱'})
    phone_number = IntegerField('手机号',
                                validators=[DataRequired(), NumberRange(1300000000, 19900000000, message='请输入正确的手机号')],
                                render_kw={'placeholder': '请输入手机号'})
    password = PasswordField('密  码', validators=[DataRequired()], render_kw={'placeholder': '请输入密码'})
    password2 = PasswordField('重复密码', validators=[DataRequired(), \
                                                  EqualTo('password', message='重复密码不一致')],
                              render_kw={'placeholder': '请再次输入密码'})
    submit = SubmitField('注  册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经注册了！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经存在！')

    def validate_phone_number(self, field):
        if User.query.filter_by(phone_number=field.data).first():
            raise ValidationError('该手机号已经存在！')


# 修改密码
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原始密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField('重复新密码',
                              validators=[DataRequired()])
    submit = SubmitField('确定')


# 密码重置
class PasswordResetRequestForm(FlaskForm):
    email = StringField('注册邮箱', validators=[DataRequired(), Length(1, 64),
                                            Email()])
    submit = SubmitField('确定')


# 密码重置
class PasswordResetForm(FlaskForm):
    password = PasswordField('新密码', validators=[
        DataRequired(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField('重复新密码', validators=[DataRequired()])
    submit = SubmitField('确定')


# 修改邮箱
class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[DataRequired(), Length(1, 64),
                                           Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('这个邮箱已经注册了')


# 修改手机号
class ChangePhoneNumberForm(FlaskForm):
    phone_number = IntegerField('手机号',
                                validators=[DataRequired(), NumberRange(1300000000, 19900000000, message='请输入正确的手机号')],
                                render_kw={'placeholder': '请输入手机号'})
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('确定')

    def validate_phone_number(self, field):
        if User.query.filter_by(phone_number=field.data).first():
            raise ValidationError('这个手机号已经注册了')

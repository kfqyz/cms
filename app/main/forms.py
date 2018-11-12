from flask_wtf import FlaskForm
from ..models import User, Role
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Email, Regexp, ValidationError


class EditProfileForm(FlaskForm):
    name = StringField('姓名', validators=[Length(0, 64)])
    phone_number = IntegerField('手机号', validators=[NumberRange(10000000000, 19000000000, message='请输入正确的手机号')])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email])
    username = StringField('用户名', validators=[DataRequired(), Length(0, 64), \
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                                                     '用户名必须只能由字母、数字、下划线、点组成')])
    confirmed = BooleanField('验证')
    role = SelectField('角色', coerce=int)
    name = StringField('姓名', validators=[Length(0, 64)])
    phone_number = IntegerField('手机号', validators=[NumberRange(10000000000, 19000000000, message='请输入正确的手机号')])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]

        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经注册了。')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经注册了。')

    def validate_phone_number(self, field):
        if field.data != self.user.phone_number and User.query.filter_by(phone_number=field.data).first():
            raise ValidationError('该手机号已经注册了。')

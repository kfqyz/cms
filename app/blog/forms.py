from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField, SelectField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Length, NumberRange, Email, Regexp, ValidationError

# 用户修改个人资料
from app.models.category import Category
from app.models.role import Role
from app.models.user import User


class EditProfileForm(FlaskForm):
    name = StringField('姓名', validators=[Length(0, 64)])
    phone_number = IntegerField('手机号', validators=[NumberRange(10000000000, 19000000000, message='请输入正确的手机号')])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提 交')


# 管理员修改用户资料
class EditProfileAdminForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[DataRequired(), Length(0, 64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须只能由字母、数字、下划线、点组成')])
    confirmed = BooleanField('验证')
    role = SelectField('角色', coerce=int)
    name = StringField('姓名', validators=[Length(0, 64)])
    phone_number = IntegerField('手机号', validators=[NumberRange(10000000000, 19000000000, message='请输入正确的手机号')])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提 交')

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


# 发布、修改文章
class PostForm(FlaskForm):
    title = StringField('文章标题', validators=[DataRequired()])
    body = TextAreaField('文章内容', render_kw={'placeholder': '文章内容', 'id': 'editor'})
    categorys = SelectMultipleField('文章分类', coerce=int)
    tags = StringField('文章标签', render_kw={'placeholder': '多个标签请用空格隔开'})
    submit = SubmitField('提 交')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        user = current_user._get_current_object()
        self.categorys.choices = [(category.id, category.name) for category in
                                  Category.query.filter_by(user=user).all()]


# 提交评论
class CommentForm(FlaskForm):
    body = StringField('', validators=[DataRequired()], render_kw={'placeholder': '输入评论内容'})
    submit = SubmitField('提 交')

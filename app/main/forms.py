from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length,NumberRange


class EditProfileForm(FlaskForm):
    name = StringField('姓名',validators=[Length(0,64)])
    phone_number = IntegerField('手机号',validators=[NumberRange(10000000000,19000000000,message='请输入正确的手机号')])
    location = StringField('位置',validators=[Length(0,64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('你的姓名：', validators=[DataRequired()])
    submit = StringField('确定')

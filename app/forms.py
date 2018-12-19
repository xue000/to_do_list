from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, PasswordField, DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(1,20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(5,20)])
    submit = SubmitField('Log in')

class TaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()])

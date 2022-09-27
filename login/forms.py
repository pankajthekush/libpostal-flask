from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField
from wtforms import validators, SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
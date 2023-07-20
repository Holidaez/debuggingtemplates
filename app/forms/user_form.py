from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign Up!')

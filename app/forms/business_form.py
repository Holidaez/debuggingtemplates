from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import Business

cats = ["American", "Mexican", "Chinese"]
class BusinessForm(FlaskForm):
    name = StringField('Name', validators=DataRequired())
    category = SelectField('Category', choices=cats, validators=DataRequired())
    desc = TextAreaField('Description', validators=DataRequired(), Length(min=3,max=100))
    submit = SubmitField('List it!')

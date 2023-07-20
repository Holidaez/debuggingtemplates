from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import Review

class ReviewForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=3, max=320)])

    submit = SubmitField('Share')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LetterButton(FlaskForm):
    letter = SubmitField('New Game')
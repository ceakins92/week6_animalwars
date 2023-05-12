from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-In')

class PostForm(FlaskForm):
    body = StringField('Comments', validators=[DataRequired()])
    card_name = StringField('Card Name', validators=[DataRequired()])
    card_series = StringField('Card Series', validators=[DataRequired()])
    card_number = StringField('Card Number', validators=[DataRequired()])
    card_value = StringField('Card Value', validators=[DataRequired()])
    submit = SubmitField('Publish')

class UserSearchForm(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    submit = SubmitField('Search')
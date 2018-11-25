from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class Subscription(FlaskForm):
    username = StringField('Your Name',validators=[Required()])
    email = StringField('Your Email Address',validators=[Required()])
    submit = SubmitField('subscribe')

class RegistrationForm(FlaskForm):
    first_name = StringField('Enter your first_name',validators = [Required()])
    last_name = StringField('Enter your last_name',validators = [Required()])
    username = StringField('Enter your username',validators = [Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

   


from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class CommentForm(FlaskForm):
    
    username = StringField('username ',validators=[Required()])
    comment = TextAreaField('post comment', validators=[Required()])
    submit = SubmitField('post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


   


    
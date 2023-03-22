from flask_wtf import FlaskForm
from wtforms.widgets import TextInput
from wtforms import StringField, SubmitField, TextAreaField, validators, EmailField, PasswordField
from wtforms.validators import DataRequired,InputRequired, EqualTo, Length, Optional 
 #https://wtforms.readthedocs.io/en/2.3.x/validators/
class UserInfoForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10,max=20, message="Please enter a valid phone number.")])
    address = TextAreaField('Mailing Address', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Submit')
    
# class MyTextInput(TextInput):
#     def __init__(self, error_class='has_errors'):
#         super(MyTextInput, self).__init__()
#         self.error_class = error_class

#     def __call__(self, field, **kwargs):
#         if field.errors:
#             c = kwargs.pop('class', '') or kwargs.pop('class_', '')
#             kwargs['class'] = '%s %s' % (self.error_class, c)
#         return super(MyTextInput, self).__call__(field, **kwargs)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
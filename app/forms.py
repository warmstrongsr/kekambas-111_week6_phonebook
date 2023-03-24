from flask_wtf import FlaskForm
from wtforms.widgets import TextInput
from wtforms import StringField, SubmitField, TextAreaField, validators, EmailField, PasswordField
from wtforms.validators import DataRequired,InputRequired, EqualTo, Length, Optional 


class AddressForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10,max=20, message="Please enter a valid phone number.")])
    address = TextAreaField('Mailing Address', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Submit')
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
    
    
class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        pass
            #user= User.query.filter_by(username.data).first()
            #if user is not None:
                #raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        pass
            #user= User.query.filter_by(email.data).first()
            #if user is not None:
                #raise ValidationError('Please use a different email address.')


class ManageForm(FlaskForm):
    devName   = StringField( 'Device Name', validators=[DataRequired()])
    devId     = IntegerField('Device ID',  validators=[DataRequired()])
    devType   = StringField( 'Device Type', validators=[DataRequired()])
    devVendor = StringField( 'Device Vendor', validators=[DataRequired()])
    submit    = SubmitField( 'Add Device')

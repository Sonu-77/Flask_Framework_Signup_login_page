from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)

class SignupForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),Length(2,35)])

    email=StringField('Email',validators=[DataRequired(),Email()])

    gender=SelectField('Gender',choices=['Male','Female','Other'],validators=[Optional()])

    dod=DateField('Data of Birth',validators=[Optional()])

    password=PasswordField('Password',validators=[DataRequired(),Length(3,20)])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),Length(3,20),EqualTo('password')])

    submit=SubmitField('SignUp')


class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])

    password=PasswordField('Password',validators=[DataRequired(),Length(3,25)])

    remember_me=BooleanField('Remember Me')

    submit=SubmitField('Login')


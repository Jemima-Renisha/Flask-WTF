from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators

class ContactForm(FlaskForm):
    name = StringField("Candidate Name", [validators.DataRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address", [validators.Optional()])
    Age = IntegerField("Age", [validators.NumberRange(min=0, max=120, message="Age must be between 0 and 120.")])
    language = SelectField("Programming Languages", choices=[('java', 'Java'), ('py', 'Python')])
    submit = SubmitField("Submit")

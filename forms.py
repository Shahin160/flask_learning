# from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField, validators, ValidationError
from wtforms.validators import DataRequired, Length, Email

# def validate_email(form, fiel):
#         if not "@gmail.com" in fiel.data:
#             raise ValidationError("Field must be with @gmail.com")


class ContactForm(FlaskForm):
    full_name = StringField(label='Your Name', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length()])
    services = SelectField(label='Needed Services', choices=[("", 'Choose Services'),('ost', 'Online Store'), ('ecb', 'eCommerce Business'), ('des', 'UI/UX Design'), ('ose', 'Online Services')])
    budget = SelectField(label='Budget', choices=[("", 'Select Budget'),(1500, '1500$'), (2000, '2000$'), (2500, '2500$')])
    message = TextAreaField(label='Message', render_kw={"placeholder": "Your message here..."})
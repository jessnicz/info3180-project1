from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class AddProperty(FlaskForm):
    title = StringField("Property Title", validators = [DataRequired()])
    description = TextAreaField("Description", validators = [DataRequired()])
    num_bedrooms = StringField("No. of Rooms", validators = [DataRequired()])
    num_bathrooms = StringField("No. of Bathrooms", validators = [DataRequired()])
    price = StringField("Price", validators = [DataRequired()])
    property_type = SelectField("Property Type", choices = ['House', 'Apartment'])
    location = StringField("Location", validators = [DataRequired()])
    photo = FileField("Photo", validators = [FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], "Unacceptable file format")])
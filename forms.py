from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, NumberRange, URL

"""Forms"""

class AddPetForm(FlaskForm):
    """Form for adding new pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    species = StringField("Species", validators=[InputRequired(message="Please enter a species"), AnyOf(['cat', 'Cat', 'dog', 'Dog', 'porcupine', 'Porcupine', 'hedgehog', 'Hedgehog'], message='Species not a valid type')])
    age = IntegerField("Age", validators=[NumberRange(0, 30, message="Please enter an appropriate age (0-30)")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Additional Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing existing pets."""

    photo_url = StringField("Photo URL", validators=[Optional()])
    notes = TextAreaField("Additional Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])
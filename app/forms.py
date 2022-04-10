# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import InputRequired, DataRequired , Length

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired(),InputRequired(),Length(max=700)])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png','Images only!'])])
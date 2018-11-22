from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, HiddenField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class AddProduct(FlaskForm):
    name = StringField('Name')
    price = IntegerField('Price')
    stock = IntegerField('Stock')
    description = TextAreaField('Description')
    # image1 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    # image2 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    # image3 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    # image4 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    # image5 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    # image6 = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
class AddImage(FlaskForm):
    image             = FileField('Image', validators=[FileAllowed(IMAGES, 'Only images are accepted.')])
    products_choices   = SelectField('Product:', validators=[DataRequired(), Optional(strip_whitespace=True)], coerce = int)

from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DecimalField, BooleanField, DateField
from wtforms.validators import DataRequired, NumberRange, Length


class ItemForm(FlaskForm):
    happiness = IntegerField("happiness", validators=[DataRequired()])
    imageUrl = StringField("imageUrl", validators=[DataRequired(), NumberRange(min =0, max=255, message="Please enter a valid imageUrl")])
    name = StringField("Name", validators=[DataRequired(), Length(min =0, max=255, message="must be between 3 and 255 characters")])
    price = IntegerField("price", validators=[DataRequired()])
    pokemonId = IntegerField("pokemonId", validators=[DataRequired()])
    createdAt = DateField("createdAt", validators=[DataRequired()])
    updatedAt = DateField("updatedAt", validators=[DataRequired()])

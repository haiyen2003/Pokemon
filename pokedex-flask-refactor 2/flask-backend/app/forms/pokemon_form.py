from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DecimalField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length


class PokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min =0, max=100, message="Please enter a valid number")])
    defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(min =0, max=100, message="Please enter a valid number")])
    imageUrl = StringField("ImageUrl", validators=[DataRequired(), Length(min =6, max=100, message="Please enter a valid email")])
    name = StringField("Name", validators=[DataRequired(), Length(min =3, max=255, message="must be between 3 and 255 characters")])
    type = StringField("Type", validators=[DataRequired()])
    moves = StringField("Moves", validators=[DataRequired(), Length(min =0, max=100, message="Please enter a valid moves")])
    encounterRate = DecimalField("EncounterRate", validators=[DataRequired(), NumberRange(min =0, max=100, message="Please enter a valid rate")], places=2)
    catchRate = DecimalField("CatchRate", validators=[DataRequired(), NumberRange(min =0, max=100, message="Please enter a valid rate")], places=2)
    capture = BooleanField("Capture")


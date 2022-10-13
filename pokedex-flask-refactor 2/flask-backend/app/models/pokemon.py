from email.policy import default
from wsgiref.validate import validator
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
db = SQLAlchemy()
from sqlalchemy.orm import validates

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable = False)
    defense = db.Column(db.Integer, nullable = False)
    imageUrl = db.Column(db.String, nullable = False)
    name = db.Column(db.String(255), nullable= False)
    type = db.Column(db.Enum, nullable = False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Float)
    catchRate = db.Column(db.Float)
    captured = db.Column(db.Boolean)
    createdAt = db.Column(db.DateTime(timezone=True), server_default = func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), onupdate = func.now())

    items = db.relationship("Items", back_populates='pokemon')

@validates("name")
def validate_name(self, str, name):
    if len(str) > 255 or len(str) < 0:
        raise ValueError('name length should be from 0 - 255 characters')
    return name

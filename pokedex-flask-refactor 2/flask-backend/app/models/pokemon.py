from .db import db
from sqlalchemy.orm import validates
from datetime import datetime

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable = False)
    defense = db.Column(db.Integer, nullable = False)
    imageUrl = db.Column(db.String, nullable = False)
    name = db.Column(db.String(255), nullable= False)
    type = db.Column(db.Enum, nullable = False)
    moves = db.Column(db.String(255), nullable=True)
    encounterRate = db.Column(db.Float)
    catchRate = db.Column(db.Float)
    captured = db.Column(db.Boolean)
    createdAt = db.Column(db.DateTime, nullable = False, default= datetime.now())
    updatedAt = db.Column(db.DateTime, nullable = False, default= datetime.now())

    items = db.relationship("Item", back_populates='pokemon')

    @validates("name")
    def validate_name(self,key, str):
        if len(str) > 255 or len(str) < 0:
            raise ValueError('name length should be from 0 - 255 characters')
        return str

    @validates("number")
    def validate_number(self, key, input):
        if input < 1:
            raise ValueError('number must be larger than 1')
        return input

    @validates("attack")
    def validate_attack(self, key, input):
        if input < 0 or input > 100:
            raise ValueError("attack must be smaller than 100 and larger than 0")
        return input

    @validates("defense")
    def validate_defense(self,key, input):
        if input < 0 or input > 100:
            raise ValueError("defense must be smaller than 100 and larger than 0")
        return input

    @validates("imageUrl")
    def validate_imageUrl(self,key, input):
        UNKNOWN_IMG_URL = "/images/unknown.png"
        if input not in ".com" or ".org" or ".net" or "www." or ".png":
            return UNKNOWN_IMG_URL


    @validates('moves')
    def validate_moves(self,key, input):
        pass


    @validates('encounterRate')
    def validate_encounter_rate(self, key, input):
        if input < 0 or input > 100:
            raise ValueError('encounterRate must be larger than 0 and less than 100')
        return input


    @validates('catchRate')
    def validate_catch_rate(self,key, input):
        if input < 0 or input > 100:
            raise ValueError('encounterRate must be larger than 0 and less than 100')
        return input


    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'attack': self.attack,
            'defense': self.defense,
            'imageUrl': self.imageUrl,
            'name': self.name,
            'type': self.type,
            'moves': self.moves,
            'encounterRate': self.encounterRate,
            'catchRate': self.catchRate,
            'captured': self.captured,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }

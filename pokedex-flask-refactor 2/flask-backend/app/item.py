from .db import db
from datetime import datetime

class item(db.Model):
    __tablename__= "types"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    pokemonId = db.Column(db.Integer, db.ForeignKey('pokemons.id'))

    createdAt = db.Column(db.Datetime, nullable = False, default= datetime.now())
    updatedAt = db.Column(db.Datetime, nullable = False, default= datetime.now())

    pokemons= db.relationship('Pokemon', back_populates ='items')


    def to_dict(self):
        return {
            'id': self.id,
            'happiness': self.happiness,
            'imageUrl': self.imageUrl,
            'name': self.name,
            'price': self.price,
            'pokemonId': self.pokemonId,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }

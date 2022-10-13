from .db import db

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
];

class pokemonType(db.Model):
    __tablename__= "types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
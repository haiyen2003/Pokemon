from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class Item(db.Model):
    __tablename__ ='items'
    id = db.Column(db.Integer, primary_key = True)
    happiness = db.Column(db.Integer, nullable = False)
    imageUrl = db.Column(db.String(255), nullable = False)
    name = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    pokemonId = db.Column(db.Integer, nullable = False)
    createdAt = db.Column(db.Date, default = datetime.now(), nullable = False)
    updatedAt = db.Column(db.Date, default = datetime.now(), nullable = False)

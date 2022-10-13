from flask import Blueprint
from ..models import db, PokemonType

pokemon_route = Blueprint('pokemonroute', __name__, url_prefix="/")


@pokemon_route.route('/')
def all_pokemon():
    pokemon = PokemonType.query.all()

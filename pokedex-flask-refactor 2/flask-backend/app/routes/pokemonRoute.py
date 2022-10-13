from flask import Blueprint
from ..models import db, PokemonType, Pokemon

bp = Blueprint('pokemonroute', __name__, url_prefix="/")


@bp.route('/')
def all_pokemon():
    pokemons = Pokemon.query.all()
    return {'pokemons': [pokemon.to_dict() for pokemon in pokemons]}

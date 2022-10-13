from flask import Blueprint
from app.models import db, PokemonType, Pokemon
from app.forms import PokemonForm



pokenmon_routes = Blueprint('pokemonroute', __name__, url_prefix="/")


@pokenmon_routes.route('/')
def all_pokemon():
    pokemons = Pokemon.query.all()
    return {'pokemons': [pokemon.to_dict() for pokemon in pokemons]}


@pokenmon_routes('/', methods=['POST'])
def add_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        newPokemon = Pokemon(

            number =form.data['number'],
            attack = form.data['attack'],
            defense = form.data['defense'],
            imageUrl = form.data['imageUrl'],
            name = form.data['name'],
            type= form.data['type'],
            moves = form.data['moves'],
            encounter = form.data['encounter'],
            catchRate =form.data['catchRate'],
            capture = form.data['capture']
        )
        db.session.add(newPokemon)
        db.session.commit()
        return newPokemon.to_dict()



@pokenmon_routes.route('/<int:id', methods=['PUT'])
def edit_pokemon(id):
    form = PokemonForm
    if form.validate_on_submit():
        editpokemon = Pokemon.query.get(id)
        editpokemon.number = form.data['number']
        editpokemon.attack = form.data['attack']
        editpokemon.defense = form.data['defense']
        editpokemon.imageUrl = form.data['imageUrl']
        editpokemon.name = form.data['name']
        editpokemon.type = form.data['type']
        editpokemon.moves= form.data['moves']
        editpokemon.encounterRate= form.data['encounterRate']
        editpokemon.catchRate= form.data['catchRate']
        editpokemon.capture= form.data['capture']

        db.session.add(editpokemon)
        db.session.commit()
        return editpokemon.to_dict()

@pokenmon_routes.route('/<int:id')
def one_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()



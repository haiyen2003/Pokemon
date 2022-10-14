from flask.cli import AppGroup
from .pokemon import seed_pokemons, undo_pokemons
from .item import seed_items, undo_items

seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    seed_pokemons()
    seed_items()


@seed_commands.command('undo')
def undo():
    undo_items()
    undo_pokemons()

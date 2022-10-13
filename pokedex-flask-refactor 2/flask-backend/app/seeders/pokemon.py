# 15 seeded Pokemon
from app.models import db, Pokemon


def seed_pokemons():
    pokemon01 = Pokemon(
        number= 1,
        imageUrl= '/images/pokemon_snaps/1.svg',
        name= 'Bulbasaur',
        attack= 49,
        defense= 49,
        type= 'grass',
        moves=
          'tackle, vine whip',
        captured= True
    )
    pokemon02 = Pokemon(
        number= 2,
        imageUrl= '/images/pokemon_snaps/2.svg',
        name= 'Ivysaur',
        attack= 62,
        defense= 63,
        type= 'grass',
        moves=
          'tackle, vine whip, razor leaf'
        ,
        captured= True
    )
    pokemon03 = Pokemon(
        number= 3,
        imageUrl= '/images/pokemon_snaps/3.svg',
        name= 'Venusaur',
        attack= 82,
        defense= 83,
        type= 'grass',
        moves=
          'tackle, vine whip,razor leaf'
        ,
        captured= True
    )
    pokemon04 = Pokemon(
        number= 4,
        imageUrl= '/images/pokemon_snaps/4.svg',
        name= 'Charmander',
        attack= 52,
        defense= 43,
        type= 'fire',
        moves=
          'scratch, ember, metal claw'
        ,
        captured= True
    )
    pokemon05 = Pokemon(
        number= 5,
        imageUrl= '/images/pokemon_snaps/5.svg',
        name= 'Charmeleon',
        attack= 64,
        defense= 58,
        type= 'fire',
        moves=
          'scratch, ember, metal claw, flamethrower'
        ,
        captured= True
    )
    pokemon06 = Pokemon(
        number= 6,
        imageUrl= '/images/pokemon_snaps/6.svg',
        name= 'Charizard',
        attack= 84,
        defense= 78,
        type= 'fire',
        moves=
          'flamethrower,wing attack,slash,metal claw',
        captured= True
    )
    pokemon07 = Pokemon(
        number= 7,
        imageUrl= '/images/pokemon_snaps/7.svg',
        name= 'Squirtle',
        attack= 48,
        defense= 65,
        type= 'water',
        moves=
          'tackle,bubble,water gun'
        ,
        captured= True
    )
    pokemon08 = Pokemon(
        number= 8,
        imageUrl= '/images/pokemon_snaps/8.svg',
        name= 'Wartortle',
        attack= 63,
        defense= 80,
        type= 'water',
        moves=
          'tackle,bubble,water gun,bite',
    )
    pokemon09 = Pokemon(
        number= 9,
        imageUrl= '/images/pokemon_snaps/9.svg',
        name= 'Blastoise',
        attack= 83,
        defense= 100,
        type= 'water',
        moves=
          'hydro pump,bubble,water gun,bite',
    )
    pokemon010 = Pokemon(
        number= 10,
        imageUrl= '/images/pokemon_snaps/10.svg',
        name= 'Caterpie',
        attack= 30,
        defense= 35,
        type= 'bug',
        moves=
          'tackle'
        ,
    )
    pokemon011 = Pokemon(
        number= 12,
        imageUrl= '/images/pokemon_snaps/12.svg',
        name= 'Butterfree',
        attack= 45,
        defense= 50,
        type= 'bug',
        moves=
          'confusion,gust,psybeam,silver wind'
        ,
    )
    pokemon012 = Pokemon(
        number= 13,
        imageUrl= '/images/pokemon_snaps/13.svg',
        name= 'Weedle',
        attack= 35,
        defense= 30,
        type= 'bug',
        moves=
          'poison sting'
        ,
    )
    pokemon013 = Pokemon(
        number= 16,
        imageUrl= '/images/pokemon_snaps/16.svg',
        name= 'Pidgey',
        attack= 45,
        defense= 40,
        type= 'normal',
        moves=
          'tackle,gust',
    )
    pokemon014 = Pokemon(
        number= 17,
        imageUrl= '/images/pokemon_snaps/17.svg',
        name= 'Pidgeotto',
        attack= 60,
        defense= 55,
        type= 'normal',
        moves=
          'tackle,gust,wing attack',
    )
    pokemon015 = Pokemon(
        number= 18,
        imageUrl= '/images/pokemon_snaps/18.svg',
        name= 'Pidgeot',
        attack= 80,
        defense= 75,
        type= 'normal',
        moves=
          'tackle,gust,wing attack',
    )

    db.session.add_all([pokemon01,pokemon02,pokemon03,pokemon04,pokemon05,pokemon06,pokemon07,pokemon08,pokemon09,pokemon010,pokemon011,pokemon012,pokemon013,pokemon014,pokemon015])
    db.session.commit()

def undo_pokemons():
    db.session.excute('TRUNCATE pokemons RESTART IDENTITY CASCADE;')
    db.session.commit()

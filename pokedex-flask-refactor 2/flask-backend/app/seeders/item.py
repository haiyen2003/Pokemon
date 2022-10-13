#10 seeded Items
from app.models import db, item

def seed_items():
    item01 = item(
    pokemonId =1,
    name='Charizard',
    price=10,
    happiness=10,
    imageUrl= "/images/pokemon_egg.svg"
    )
    item02 = item(
    pokemonId =2,
    name='Charizard',
    price=20,
    happiness=20,
    imageUrl= "/images/pokemon_egg.svg"
    )
    item03= item(
    pokemonId =3,
    name='Venusaur',
    price=30,
    happiness=30,
    imageUrl='/images/pokemon_snaps/3.svg',
    )
    item04= item(
    pokemonId =4,
    name='Charmander',
    price=40,
    happiness=40,
    imageUrl='/images/pokemon_snaps/4.svg',

    )
    item05= item(
    pokemonId =5,
    name='Charmeleon',
    price=50,
    happiness=50,
    imageUrl='/images/pokemon_snaps/5.svg',
    )

    item06 = item(
    pokemonId =6,
    name='Charizard',
    price=60,
    happiness=60,
    imageUrl= "/images/pokemon_egg.svg",
  )
    item07 = item(
    pokemonId =7,
    name='Squirtle',
    price=70,
    happiness=70,
    imageUrl= '/images/pokemon_snaps/8.svg',

  )
    item08= item(
    pokemonId =8,
    name='Wartortle',
    price=80,
    happiness=80,
    imageUrl= 'images/pokemon_snaps/8.svg',

    )
    item09= item(
    pokemonId =9,
    name='Wartortle',
    price=90,
    happiness=90,
    imageUrl='/images/pokemon_snaps/9.svg',

    )
    item10= item(
    pokemonId =10,
    name='Caterpie',
    price=95,
    happiness=95,
    imageUrl='/images/pokemon_snaps/10.svg',

      )


    db.session.add_all([item01,item02,item03,item04,item05,item06,item07,item08,item09,item10])
    db.session.commit()

def undo_items():
    db.session.excute('TRUNCATE pokemons RESTART IDENTITY CASCADE;')
    db.session.commit()

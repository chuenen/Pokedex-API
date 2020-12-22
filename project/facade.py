from .db import transaction
from .models import Pokemon, Evolution
from .repos import pokemon_repo, type_repo, evolution_repo


@transaction()
def get_pokemon(pokemon_id):
    return pokemon_repo.get(pokemon_id).to_dict()

@transaction()
def add_pokemon(data):
    pokemon = Pokemon(number=data['number'], name=data['name'])
    for type_ in data['types']:
        t = type_repo.get_or_create(type_)
        if t:
            pokemon.types.append(t)
    return pokemon_repo.add(pokemon).to_dict()

@transaction()
def update_pokemon(pokemon_id, body):
    types = [type_repo.get_or_create(type_) for type_ in body['types']]
    pokemon = pokemon_repo.get(pokemon_id)
    pokemon.number = body['number']
    pokemon.name = body['name']
    pokemon.types = types
    return pokemon.to_dict()

@transaction()
def delete_pokemon(pokemon_id):
    pokemon_repo.remove(pokemon_id)

@transaction()
def list_pokemons(type_):
    if type_:
        pokemons = pokemon_repo.find(type_)
    else:
        pokemons = pokemon_repo.list()

    return [pokemon.to_dict() for pokemon in pokemons]

@transaction()
def add_evolution(pokemon_id, evolution_id):
    evolution = evolution_repo.get(pokemon_id, evolution_id)
    if not evolution:
        pokemon = pokemon_repo.get(evolution_id)
        evolution = Evolution(pokemon_id=pokemon_id, evolution_id=evolution_id)
        evolution_repo.add(evolution)
    return pokemon_repo.get(pokemon_id).to_dict()

@transaction()
def delete_evolution(pokemon_id, evolution_id):
    evolution_repo.remove(pokemon_id, evolution_id)
    return pokemon_repo.get(pokemon_id).to_dict()


# vi:et:ts=4:sw=4:cc=80

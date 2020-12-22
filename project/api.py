from flask import request, jsonify
from connexion import NoContent

from . import facade
from .repos import pokemon_repo
from .exceptions import PokemonNotFound


def get_pokemon(pokemon_id):
    try:
        data = facade.get_pokemon(pokemon_id)
    except PokemonNotFound:
        return NoContent, 404
    return jsonify(data)

def add_pokemon(body):
    pokemon_id = facade.add_pokemon(body)
    return jsonify({'pokemon_id': pokemon_id}), 201

def update_pokemon(pokemon_id, body):
    data = facade.update_pokemon(pokemon_id, body)
    return jsonify(data)

def delete_pokemon(pokemon_id):
    facade.delete_pokemon(pokemon_id)
    return 'ok', 200

def list_pokemons():
    type_ = request.args.get('type')
    pokemons = facade.list_pokemons(type_)
    return jsonify(pokemons)

def add_evolution(pokemon_id, evolution_id):
    try:
        pokemon = facade.add_evolution(pokemon_id, evolution_id)
    except PokemonNotFound:
        return NoContent, 404
    return jsonify(pokemon)

def delete_evolution(pokemon_id, evolution_id):
    try:
        pokemon = facade.delete_evolution(pokemon_id, evolution_id)
    except PokemonNotFound:
        return NoContent, 404
    return jsonify(pokemon)


# vi:et:ts=4:sw=4:cc=80

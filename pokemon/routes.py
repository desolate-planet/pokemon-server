from flask import Blueprint

from pokemon.service import pokemon_service

main = Blueprint("main", __name__)


@main.route("/pokemon/api/v1")
def get_all_pokemon():
    pokemon_data = pokemon_service.get_pokemon_data()
    if not pokemon_data:
        return "Unable to retrieve pokemon data", 500
    return pokemon_service.get_pokemon_data()

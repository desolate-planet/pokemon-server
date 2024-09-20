# !/usr/bin/env python
# pokemon_service.py
import requests
import random


def get_pokemon_data():
    """Returns a shuffled of Pokemon returned by the PokeAPI."""
    pokemon = retrieve_all_pokemon()
    random.shuffle(pokemon)
    return pokemon


def retrieve_all_pokemon():
    """Queries the pokeapi for the first 50 Pokemon"""
    url = "http://pokeapi.co/api/v2/pokemon?limit=50"
    # A GET request to the API
    response = requests.get(url)

    if response.status_code != 200:
        print('Unable to retrieve pokemon')
        return []

    return response.json().get("results")

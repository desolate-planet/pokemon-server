# !/usr/bin/env python
from flask import Flask
from pokemon.service import pokemon_service

app = Flask(__name__)


@app.route("/pokemon/api/v1")
def get_pokemon():
    return pokemon_service.get_pokemon_data()

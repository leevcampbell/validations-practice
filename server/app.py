#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import exc

from models import db, PokemonCard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# CARD ROUTES #

@app.get('/cards')
def all_games():
    cards = PokemonCard.query.all()
    cards_to_dict = [card.to_dict() for card in cards]
    return cards_to_dict, 200


@app.post('/cards')
def create_game():
    return "You'll need to fix the POST to accept and process your data!"


@app.get('/cards/<int:id>')
def game_by_id(id):
    try:
        card = PokemonCard.query.where(PokemonCard.id == id).first()
        return card.to_dict(), 200
    except AttributeError:
        return {'message': 'No card found'}, 404


@app.delete('/cards/<int:id>')
def delete_game(id):
    card = PokemonCard.query.where(PokemonCard.id == id).first()
    if card:
        db.session.delete(card)
        db.session.commit()
        return {}, 204
    else:
        return {'message': 'No card found'}, 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)

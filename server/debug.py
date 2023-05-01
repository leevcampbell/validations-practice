#!/usr/bin/env python3

from app import app
from flask import Flask
from flask_migrate import Migrate
from models import PokemonCard, db
import ipdb


if __name__ == '__main__':

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    migrate = Migrate(app, db)

    db.init_app(app)

    with app.app_context():
        ipdb.set_trace()

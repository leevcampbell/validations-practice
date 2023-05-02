from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class PokemonCard(db.Model):
    __tablename__ = 'pokemon_cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique = True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    card_type = db.Column(db.String, nullable=False)
    is_holographic = db.Column(db.Boolean, nullable=False)
    # write the rest of your methods here!

    @validates('price')
    def validate_price(self, key, price):
        if price < 0:
            raise ValueError("Price must be positive")
        return price

    @validates('hp')
    def validate_hp(self, key, hp):
        if hp < 0 and hp > 100 and hp != (hp % 10):
            raise ValueError("HP must be between 0 and 100")
        return hp

    @validates('card_type')
    def validate_type(self, key, card_type):
        if card_type == "" and card_type != "Fire" and card_type != "Water" and card_type != "Grass" and card_type != "Lightning" and card_type != "Psychic" and card_type != "Fighting" and card_type != "Darkness" and card_type != "Metal" and card_type != "Fairy" and card_type != "Dragon":
            raise ValueError("Type cannot be empty")
        return card_type

    @validates('is_holographic')
    def validate_is_holographic(self, key, is_holographic):
        if self.name == "Pikachu" and is_holographic == False:
            raise ValueError("Pikachu must be holographic")
        return is_holographic

    @validates('name')
    def validate_name(self, key, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        return name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "hp": self.hp,
            "card_type": self.card_type,
            "is_holographic": self.is_holographic
        }

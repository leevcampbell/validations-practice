# Validations Practice

## Getting Started

In your terminal run `pipenv install` and `pipenv shell`. Be sure to `cd` into
the `server` directory.

## Model

You have one model PokemonCard. Build the model with:

- name (string)
- price (integer)
- hit_points (integer)
- type (string)
- is_holographic (boolean)

## Validations

Once the model has been built, add in these validations:

- all attributes must not be null

- `name` has a max of 40 characters

- `price` must be a positive number

- `hit_points` must be a number between 0 and 200

- `type` cannot be an empty string

## HARDMODE Validations

- `name` must start with a capital letter and cannot be an empty string

- `hit_points` must be divisible by 10 (so 20,30,40,etc.)

- `type` must be one of the following: `Grass`, `Fire`, `Water` (you can add
  more Pokemon types but it's unnecessary)

- `is_holographic` must be `True` if the Pokemon's name is `Pikachu`

## Testing

Routes have been created for you to test your validations in Postman. You have
access to `GET /cards`, `POST /cards`, `GET /cards/<int:id>`, and
`DELETE /cards/<int:id>`.

The POST route is missing functionality! Be sure to add it!

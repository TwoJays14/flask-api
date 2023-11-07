from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacters

def format_character(character):
  return {
    'name': character.name,
    'age': character.age,
    'catch_phrase': character.catch_phrase
  }

@app.route('/') # set route just like express/node
def hello_world(): 
  return '<p>Hello World</p>'

@app.route('/characters', methods=['POST'])
def create_character():
  data = request.get_json() # parses JSON data from request
  character = FriendsCharacters(**data) # unpacking syntax - allows creation of object with all attributes without explicitly naming them
  db.session.add(character)
  db.session.commit()
  return jsonify(id=character.id, **data)

@app.route('/characters', methods=['GET'])
def get_characters():
  characters = FriendsCharacters.query.all()
  character_list = [format_character(character) for character in characters] # for loop placed with list comprehension, list comprehension iterates over character, applying the format_character function to each character whilst creating the character list in a single line
  return {'characters': character_list}

@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
  character = FriendsCharacters.query.get(id) # gets character by its primary key
  # error handling
  if character is None:
    abort(404)
    
  character_data = {
    'id': character.id,
    'name': character.name,
    'age': character.age,
    'catch_phrase': character.catch_phrase
  }
    
  return jsonify(**character_data)

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
  character = FriendsCharacters.query.get(id)
  
  if character is None:
    abort(404)
    
  db.seesion.delete(character)
  db.session.commit()
  
  return 'Character deleted'

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
  character = FriendsCharacters.query.get(id) # gets character by its primary key
  #error handling
  if character is None:
    abort(404)
    
  data = request.get_json()
  # The loop iterates over the keys and values in the data dictionary and uses the setattr function to update the character object's attributes.
  for key, value in data.items(): 
    setattr(character, key, value)
  
  db.session.commit()
  
  return jsonify(id=character.id, **data)
  
  
  

# Manages the various game components (Database, game itself)

import fish_db
import game

import discord_input_adapter as dia

# Loads the game from database based on username
# If it does not exist, creates an entry instead
async def load_game(PLAYER_USERNAME):
  if fish_db.save_file_exists(PLAYER_USERNAME):
    return fish_db.get_save_file(PLAYER_USERNAME)
  else:
    return new_save()

def new_save():
  return {"money": 0} 

def save_game():
  pass  

def update_state(raw_player_input, game_state):
  converted_player_input = dia.convert_input(raw_player_input)
  if converted_player_input == None:
    return None

  game_state = game.update_state(converted_player_input, game_state)

  return game_state

# Manages the various game components (Database, game itself)

import fish_db
import game

import discord_input_adapter as dia

# Loads the game from database based on username
# If it does not exist, creates an entry instead
async def load_game(PLAYER_USERNAME):
  print("Loading user save file")
  if fish_db.save_file_exists(PLAYER_USERNAME):
    return fish_db.get_save_file(PLAYER_USERNAME)
  else:
    print("User does not exist")
    fish_db.create_save_file(PLAYER_USERNAME)
    print("Created new user")
    return fish_db.get_save_file(PLAYER_USERNAME)

def save_game(PLAYER_USERNAME, game_state):
  fish_db.update_money(game_state["money"], PLAYER_USERNAME)

def update_state(raw_player_input, game_state):
  converted_player_input = dia.convert_input(raw_player_input)
  if converted_player_input == None:
    return None

  game_state = game.update_state(converted_player_input, game_state)

  return game_state

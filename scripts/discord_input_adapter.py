from enum import Enum
from scene.main_menu_scene import TestPlayerAction 

def is_valid_input(player_input):
  return player_input == button

def convert_discord_to_game(player_input):
  match player_input:
    case "⏺":
      return TestPlayerAction.INCREMENT
  return None

def convert_game_to_discord(game_input):
  match game_input:
    case TestPlayerAction.INCREMENT:
      return "⏺"
  return None

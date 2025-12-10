from enum import Enum
from game import TestPlayerAction 

def is_valid_input(player_input):
  return player_input == button

def convert_input(player_input):
  match player_input:
    case "⏺":
      return TestPlayerAction.INCREMENT
  return None

from enum import Enum
import math
import random

class TestPlayerAction(Enum):
  INCREMENT = 0

class PlayerAction(Enum):
  REEL_IN = 0
  HOLD = 1
  SLACK = 2

class FishAction(Enum):
  DASH = 0
  RESIST = 1
  REST = 2
fish_actions_array = [FishAction.DASH, FishAction.RESIST, FishAction.REST]

FISH_STAMINA = 5
ROD_LENGTH = 10
ROD_STARTING_LENGTH = math.floor(ROD_LENGTH / 2)
MAX_TENSION = 5

games = {}

def start_game(instance_id):
   games[instance_id] = new_game_state() 
   return games[instance_id]

def new_game_state():
  state = {}
  state["stamina"] = FISH_STAMINA
  state["max_stamina"] = FISH_STAMINA

  state["length"] = ROD_STARTING_LENGTH
  state["max_length"] = ROD_LENGTH
  
  state["tension"] = 0
  state["max_tension"] = MAX_TENSION

  state["fish_action"] = FishAction.DASH
  state["fish_action_history"] = [state["fish_action"]]
  return state

# Returns State of the game
# Returns None for invalid action/instance id
def take_fishing_action(instance_id, player_action):
  if not player_action in PlayerAction:
    return None
  if not instance_id in games:
    return None

  state = games[instance_id]

  # Game is over
  if state["length"] <= 0:
    return None 
  if state["tension"] > state["max_tension"]:
    return None 

  # Game rule Input validation
  if state["length"] >= state["max_length"] and player_action == PlayerAction.SLACK:
    return None

  state = update_state(player_action, state)

  # Update state and return
  games[instance_id] = state
  return state

def update_state(player_action, state):
  if player_action == None:
    return
  if player_action == TestPlayerAction.INCREMENT:
    state["money"] += 1
  return state

#def update_state(player_action, state):
#  fish_action = state["fish_action"]
#  for attribute in ["stamina", "length", "tension"]:
#    state[attribute] += action_matrix[fish_action][player_action][attribute]
#    # Values cannot go below 0
#    state[attribute] = max(0, state[attribute])
#
#  state["length"] = min(state["length"], state["max_length"])
#
#  # If fish is out of energy
#  if state["stamina"] == 0:
#    state["fish_action"] = FishAction.REST 
#  elif state["fish_action_history"][-1] == FishAction.REST:
#    # Rest based on max stamina
#    if random.random() < state["stamina"] / FISH_STAMINA:
#      state["fish_action"] = random.choice([FishAction.DASH, FishAction.RESIST])
#    else:
#      state["fish_action"] = FishAction.REST 
#  else:
#    state["fish_action"] = random.choice([FishAction.DASH, FishAction.RESIST])
#  state["fish_action_history"].append(state["fish_action"])
#  return state

action_matrix = {
FishAction.DASH :   {PlayerAction.REEL_IN: {"stamina": -2, "length": -1, "tension":  2},
                     PlayerAction.HOLD   : {"stamina": -1, "length":  0, "tension":  1},
                     PlayerAction.SLACK  : {"stamina": -1, "length":  2, "tension":  0}},
FishAction.RESIST : {PlayerAction.REEL_IN: {"stamina": -1, "length": -1, "tension":  1},
                     PlayerAction.HOLD   : {"stamina": -1, "length":  0, "tension":  0},
                     PlayerAction.SLACK  : {"stamina": -1, "length":  1, "tension":  0}},
FishAction.REST :   {PlayerAction.REEL_IN: {"stamina":  1, "length": -2, "tension":  0},
                     PlayerAction.HOLD   : {"stamina":  1, "length":  0, "tension": -1},
                     PlayerAction.SLACK  : {"stamina":  1, "length":  0, "tension": -2}}}


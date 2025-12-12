# Scene of the game.
# Represents a distinct view that has different game rules and inputs
from enum import Enum

from typing import Self, List

# Scenes have the below implementation requirements that should be implemented
# in child classes, highlighted by "TODO"

# TODO Define an Enum for this Scene's unique inputs
#class ExampleInput(Enum):
#  DO_NOTHING = 0

class Scene:
  def __init__(self, game_state):
    self.game_state = game_state

  def get_game_state(self):
    return self.game_state

  # TODO On Player input, return the next scene
  async def enter_player_input(self, raw_player_input) -> Self:
    return self

  # TODO Add a list of required inputs as an Enum
  def get_required_inputs() -> List[Enum]:
    return []

class MainMenuScene(Scene):
  def test_scene(self):
    print("Scene is working!")

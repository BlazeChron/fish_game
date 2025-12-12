from scene.scene import Scene
from enum import Enum
from typing import Self, List

class TestPlayerAction(Enum):
  INCREMENT = 0

class MainMenuScene(Scene):
  def test_scene(self):
    print("Scene is working!")

  # TODO On Player input, return the next scene
  async def enter_player_input(self, player_action) -> Self:
    if player_action == None:
      return self
    if player_action == TestPlayerAction.INCREMENT:
      self.game_state["money"] += 1
    return self

  # TODO Add a list of required inputs as an Enum
  def get_required_inputs() -> List[Enum]:
    return []


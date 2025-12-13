from scene.scene import Scene
from scene.dialogue_scene import DialogueScene
from scene.fish_game_scene import FishGameScene
from enum import Enum
from typing import Self, List

class MainMenuAction(Enum):
  GO_TO_DIALOGUE = 0
  GO_TO_FISH = 1

class MainMenuScene(Scene):
  async def enter_player_input(self, player_action) -> Self:
    if player_action == None:
      return self
    if player_action == MainMenuAction.GO_TO_DIALOGUE:
      #self.game_state["money"] += 1
      return DialogueScene(self)
    if player_action == MainMenuAction.GO_TO_FISH:
      return FishGameScene(self)
    return self

  def get_required_inputs(self) -> List[Enum]:
    return [MainMenuAction.GO_TO_DIALOGUE, MainMenuAction.GO_TO_FISH]


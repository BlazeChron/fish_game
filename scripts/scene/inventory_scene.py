from scene.scene import Scene
from enum import Enum
from typing import Self, List

import db_scripts.db_setup as db

class InventoryAction(Enum):
  BACK = 0

class InventoryScene(Scene):
  def __init__(self, following_scene, username):
    # Scene to load after the dialogue 
    self.following_scene = following_scene
    game_state = None
    super(InventoryScene, self).__init__(game_state, username)

  async def enter_player_input(self, player_action) -> Self:
    if player_action == None:
      return self
    if player_action == InventoryAction.BACK:
      return self.following_scene
    return self

  def get_required_inputs(self) -> List[Enum]:
    return [InventoryAction.BACK]

  def get_string(self):
    return db.get_user_fishes_as_string(self.username)

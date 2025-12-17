from scene.scene import Scene
from enum import Enum
from typing import Self, List

import db_scripts.db_setup as db

class FishGameAction(Enum):
  FISH = 0
  BACK = 1

class FishGameScene(Scene):
  def __init__(self, following_scene, username):
    # Scene to load after the game 
    self.following_scene = following_scene
    game_state = {"caught": []}
    super(FishGameScene, self).__init__(game_state, username)

  async def enter_player_input(self, player_action) -> Self:
    if player_action == None:
      return self
    if player_action == FishGameAction.FISH:
      fish = db.create_fish(self.username)
      self.get_game_state()["caught"].append(fish)
    if player_action == FishGameAction.BACK:
      return self.following_scene
    return self

  def get_required_inputs(self) -> List[Enum]:
    return [FishGameAction.FISH, FishGameAction.BACK]


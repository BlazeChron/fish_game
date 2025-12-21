from scene.scene import Scene
from enum import Enum
from typing import Self, List

class DialogueAction(Enum):
  NEXT = 0
  NEXT_SCENE = 1

class DialogueScene(Scene):
  def __init__(self, following_scene, username):
    self.load_dialogue()
    # Scene to load after the dialogue 
    self.following_scene = following_scene
    game_state = {"text": self.dialogue[self.dialogue_index]}
    super(DialogueScene, self).__init__(game_state, username)

  async def enter_player_input(self, player_action) -> Self:
    if player_action == None:
      return self
    if player_action == DialogueAction.NEXT:
      # Protect from out of bounds, possible from spamming
      if self.dialogue_index >= len(self.dialogue):
        return self

      # TODO Actual race condition if you spam
      self.dialogue_index += 1
      self.get_game_state()["text"] = self.dialogue[self.dialogue_index]
    if player_action == DialogueAction.NEXT_SCENE:
      return self.following_scene
    return self

  def get_required_inputs(self) -> List[Enum]:
    if self.dialogue_index >= len(self.dialogue) - 1:
      return [DialogueAction.NEXT_SCENE]
    return [DialogueAction.NEXT]

  def load_dialogue(self):
    self.dialogue = ["First Dialogue Box", "Second Dialogue Box", "Third Dialogue Box"]
    self.dialogue_index = 0

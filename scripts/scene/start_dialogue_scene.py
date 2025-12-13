import scene.dialogue_scene
from enum import Enum
from typing import Self, List

class StartDialogueScene(scene.dialogue_scene.DialogueScene):
  def load_dialogue(self):
    self.dialogue = ["Imagine a stunning opening cinematic", "oooOOoooo", "End :)"]
    self.dialogue_index = 0

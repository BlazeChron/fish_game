
from scene.main_menu_scene import MainMenuScene, MainMenuAction 
from scene.dialogue_scene import DialogueScene, DialogueAction 
from scene.fish_game_scene import FishGameScene, FishGameAction
from scene.inventory_scene import InventoryScene, InventoryAction

#def state_to_string(state):
#  return "money: {money}".format(**state)

def scene_to_string(scene):
  if isinstance(scene, MainMenuScene):
    state = scene.get_game_state()
    return """
This is the main menu
You have : f${money}
""".format(**state) + """
Dialogue, Go fish
"""
  if isinstance(scene, DialogueScene):
    state = scene.get_game_state()
    return """
\"
{text}
\"
""".format(**state) + """
Next:
"""

  if isinstance(scene, FishGameScene):
    state = scene.get_game_state()
    return """
You have caught: {caught}
""".format(**state) + """
Fish, Back
"""

  if isinstance(scene, InventoryScene):
    return scene.get_string()

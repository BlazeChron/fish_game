from enum import Enum
from scene.main_menu_scene import MainMenuScene, MainMenuAction 
from scene.dialogue_scene import DialogueScene, DialogueAction 

def convert_discord_to_game(player_input, scene):
  if isinstance(scene, MainMenuScene):
    match player_input:
      case "⏺":
        return MainMenuAction.GO_TO_DIALOGUE
      case "🎣":
        return MainMenuAction.GO_TO_FISH
  if isinstance(scene, DialogueScene):
    match player_input:
      case "⏺":
        return DialogueAction.NEXT
      case "👍":
        return DialogueAction.RETURN
  print("No such input")
  return None

def convert_game_to_discord(game_input, scene):
  if isinstance(scene, MainMenuScene):
    match game_input:
      case MainMenuAction.GO_TO_DIALOGUE:
        return "⏺"
      case MainMenuAction.GO_TO_FISH:
        return "🎣"

  if isinstance(scene, DialogueScene):
    match game_input:
      case DialogueAction.NEXT:
        return "⏺"
      case DialogueAction.RETURN:
        return "👍"
  return None

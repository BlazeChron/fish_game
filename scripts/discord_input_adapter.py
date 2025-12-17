from enum import Enum
from bidict import bidict

from scene.main_menu_scene import MainMenuScene, MainMenuAction 
MAIN_MENU_INPUT_MAP = bidict({
  "⏺": MainMenuAction.GO_TO_DIALOGUE,
  "🎣": MainMenuAction.GO_TO_FISH,
  "📦": MainMenuAction.GO_TO_INVENTORY
})

from scene.dialogue_scene import DialogueScene, DialogueAction 
DIALOGUE_INPUT_MAP = bidict({
  "⏺": DialogueAction.NEXT,
  "👍": DialogueAction.NEXT_SCENE
})

from scene.fish_game_scene import FishGameScene, FishGameAction
FISH_GAME_INPUT_MAP = bidict({
  "🎣": FishGameAction.FISH,
  "🔙":  FishGameAction.BACK
})

from scene.inventory_scene import InventoryScene, InventoryAction
INVENTORY_INPUT_MAP = bidict({
  "🔙":  InventoryAction.BACK
})

def convert_discord_to_game(player_input, scene):
  if isinstance(scene, MainMenuScene):
    return MAIN_MENU_INPUT_MAP[player_input]
  if isinstance(scene, DialogueScene):
    return DIALOGUE_INPUT_MAP[player_input]
  if isinstance(scene, FishGameScene):
    return FISH_GAME_INPUT_MAP[player_input]
  if isinstance(scene, InventoryScene):
    return INVENTORY_INPUT_MAP[player_input]
  print("No such player input")
  return None

def convert_game_to_discord(game_input, scene):
  if isinstance(scene, MainMenuScene):
    return MAIN_MENU_INPUT_MAP.inverse[game_input]
  if isinstance(scene, DialogueScene):
    return DIALOGUE_INPUT_MAP.inverse[game_input]
  if isinstance(scene, FishGameScene):
    return FISH_GAME_INPUT_MAP.inverse[game_input]
  if isinstance(scene, InventoryScene):
    return INVENTORY_INPUT_MAP.inverse[game_input]
  print("No such game input")
  return None

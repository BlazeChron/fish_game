# Manages the various game components (Database, game itself)

import fish_db
import game
from scene.main_menu_scene import MainMenuScene
from scene.start_dialogue_scene import StartDialogueScene

# Loads the game from database based on username
# If it does not exist, creates an entry instead
async def load_game(PLAYER_USERNAME):
  print("Loading user save file")
  if not fish_db.save_file_exists(PLAYER_USERNAME):
    print("User does not exist")
    fish_db.create_save_file(PLAYER_USERNAME)
    print("Created new user")
    save_state = fish_db.get_save_file(PLAYER_USERNAME)
    start_scene = StartDialogueScene(MainMenuScene(save_state))
    return start_scene

  # User exists
  save_state = fish_db.get_save_file(PLAYER_USERNAME)
  menu_scene = MainMenuScene(save_state)
  return menu_scene

def save_game(PLAYER_USERNAME, game_state):
  fish_db.update_money(game_state["money"], PLAYER_USERNAME)

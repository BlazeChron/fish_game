# Session class that users interact with
# Handles output
import game_manager

import game_state_string_adapter as gssa

class Session:
  def __init__(self, username, msg, game_scene):
    self.PLAYER_USERNAME = username
    self.message = msg
    self.game_scene = game_scene

  # Factory method to work around async initialisation
  @classmethod
  async def create_session(cls, username, msg):
    game_scene = await game_manager.load_game(username)
    self = cls(username, msg, game_scene)
    await msg.add_reaction("⏺")

    game_state = game_scene.get_game_state()
    new_content = gssa.state_to_string(game_state)
    await self.edit_message(new_content)

    return self

  async def enter_player_input(self, raw_player_input):
    current_game_state = self.game_scene.get_game_state()
    new_game_state = game_manager.update_state(raw_player_input, current_game_state)
    if new_game_state == None:
      return

    self.game_scene.game_state = new_game_state
    game_manager.save_game(self.PLAYER_USERNAME, new_game_state)
    new_content = gssa.state_to_string(new_game_state)
    edited_message = await self.edit_message(new_content)

  async def edit_message(self, new_content):
    edited_message = await self.message.edit(content=new_content)
    self.message = edited_message

  def get_message_id(self):
    return self.message.id

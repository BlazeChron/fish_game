# Session class that users interact with
# Handles output
import game_manager

import game_state_string_adapter as gssa

import discord_input_adapter as dia

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
    converted_player_input = dia.convert_input(raw_player_input)
    if converted_player_input == None:
      return 

    new_scene = await self.game_scene.enter_player_input(converted_player_input)

    if not new_scene == self.game_scene:
      print("Different Scene after input!")
      self.game_scene = new_scene

    new_game_state = self.game_scene.get_game_state()
    game_manager.save_game(self.PLAYER_USERNAME, new_game_state)
    new_content = gssa.state_to_string(new_game_state)
    edited_message = await self.edit_message(new_content)

  async def edit_message(self, new_content):
    edited_message = await self.message.edit(content=new_content)
    self.message = edited_message

  def get_message_id(self):
    return self.message.id

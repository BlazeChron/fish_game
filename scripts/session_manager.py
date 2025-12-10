# Manages the ongoing sessions created by Discord Bot

import discord

import game_manager

import game_state_string_adapter as gssa

# There are no race conditions in Ba Sing Se...
# Username indexed dictionary: ongoing_sessions[username]
ongoing_sessions = {}

async def create_session(PLAYER_USERNAME, original_message: discord.Message):
  SESSION_ID = original_message.id

  # On create session, remove any previous session
  if PLAYER_USERNAME in ongoing_sessions:
    previous_session = ongoing_sessions[PLAYER_USERNAME]
    await previous_session.message.delete()
    del ongoing_sessions[PLAYER_USERNAME]
  
  # sanity check
  assert PLAYER_USERNAME not in ongoing_sessions

  game_state = await game_manager.load_game(PLAYER_USERNAME)
  new_content = gssa.state_to_string(game_state)
  
  edited_message = await original_message.edit(content=new_content)
  await edited_message.add_reaction("⏺")

  ongoing_sessions[PLAYER_USERNAME] = Session(PLAYER_USERNAME, edited_message, game_state)

# Gets session of player interacting with message
def get_session(PLAYER_USERNAME):
  if not PLAYER_USERNAME in ongoing_sessions:
    return None
  return ongoing_sessions[PLAYER_USERNAME]

# Session class that users interact with
# Handles output
class Session:
  def __init__(self, username, msg, gs):
    self.PLAYER_USERNAME = username
    self.message = msg
    self.game_state = gs

  async def enter_player_input(self, raw_player_input):
    new_game_state = game_manager.update_state(raw_player_input, self.game_state)
    if new_game_state == None:
      return

    self.game_state = new_game_state
    game_manager.save_game(self.PLAYER_USERNAME, self.game_state)
    new_content = gssa.state_to_string(self.game_state)
    edited_message = await self.edit_message(new_content)

  async def edit_message(self, new_content):
    edited_message = await self.message.edit(content=new_content)
    self.message = edited_message
    return edited_message

  def get_message_id(self):
    return self.message.id

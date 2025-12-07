# Manages the ongoing sessions created by Discord Bot

import discord

import game_manager
import game

import game_state_string_adapter as gssa

# There are no race conditions in Ba Sing Se...
# Username indexed dictionary: ongoing_sessions[username]
ongoing_sessions = {}

async def create_session(PLAYER_USERNAME, original_message: discord.Message):
#  await og_response.add_reaction("◀️")
#  await og_response.add_reaction("⏺")
#  await og_response.add_reaction("▶️")
  SESSION_ID = original_message.id

# On create session, remove any previous sessions
  if PLAYER_USERNAME in ongoing_sessions:
    previous_session = ongoing_sessions[PLAYER_USERNAME]
    await previous_session.message.delete()
    # clear dictionary
    del ongoing_sessions[PLAYER_USERNAME]
  
  # sanity check
  assert PLAYER_USERNAME not in ongoing_sessions

  game_state = await game_manager.load_game(PLAYER_USERNAME)
  new_content = gssa.state_to_string(game_state)
  
  edited_message = await original_message.edit(content=new_content)
  await edited_message.add_reaction("⏺")

  ongoing_sessions[PLAYER_USERNAME] = Session(edited_message, game_state)

def is_valid_user_input(PLAYER_USERNAME, MESSAGE_ID):
  return PLAYER_USERNAME in ongoing_sessions and ongoing_sessions[PLAYER_USERNAME].message.id == MESSAGE_ID

async def enter_player_input(PLAYER_USERNAME, raw_player_input):
  game_state = ongoing_sessions[PLAYER_USERNAME].game_state

  game_state = game_manager.update_state(raw_player_input, game_state)
  if game_state == None:
    return None

  new_content = gssa.state_to_string(game_state)

  edited_message = await ongoing_sessions[PLAYER_USERNAME].message.edit(content=new_content)

  del ongoing_sessions[PLAYER_USERNAME]
  ongoing_sessions[PLAYER_USERNAME] = Session(edited_message, game_state)

class Session:
  def __init__(self, msg, gs):
    self.message = msg
    self.expiry_date = None
    self.game_state = gs

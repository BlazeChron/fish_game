# Manages the ongoing sessions created by Discord Bot

import discord

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

  edited_message = await original_message.edit(content="loaded!")
  ongoing_sessions[PLAYER_USERNAME] = Session(edited_message)

#  new_game_state = game.start_game(og_response.id)
#  state_string = game_state_to_view(new_game_state)
#  edited_message = await og_response.edit(content=state_string)
#  test_events.append([edited_message, ctx.user.global_name])

  #await ctx.followup.send("test interaction")

class Session:
  def __init__(self, msg):
    self.message = msg
    self.expiry_date = None

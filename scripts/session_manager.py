# Manages the ongoing sessions created by Discord Bot

from session import Session

# There are no race conditions in Ba Sing Se...
# Username indexed dictionary: ongoing_sessions[username]
ongoing_sessions = {}

async def create_session(PLAYER_USERNAME, original_message):
  SESSION_ID = original_message.id

  # On create session, remove any previous session
  if PLAYER_USERNAME in ongoing_sessions:
    previous_session = ongoing_sessions[PLAYER_USERNAME]
    await previous_session.message.delete()
    del ongoing_sessions[PLAYER_USERNAME]
  
  # sanity check
  assert PLAYER_USERNAME not in ongoing_sessions

  ongoing_sessions[PLAYER_USERNAME] = await Session.create_session(PLAYER_USERNAME, original_message)

# Gets session of player interacting with message
def get_session(PLAYER_USERNAME):
  if not PLAYER_USERNAME in ongoing_sessions:
    return None
  return ongoing_sessions[PLAYER_USERNAME]


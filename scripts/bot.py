#bot imports
import discord

# error logging
import logging
import traceback

import datetime

import setproctitle

import session_manager


setproctitle.setproctitle("disc_fish_game")

bot = discord.Bot()

@bot.event
async def on_ready():
  print(f'Logged on as {bot.user}')

@bot.slash_command()
async def start(ctx: discord.ApplicationContext):
  interaction = await ctx.send_response("Loading game")
  PLAYER_USERNAME = ctx.user.global_name
  og_response = await interaction.original_response()

  await session_manager.create_session(PLAYER_USERNAME, og_response)


@bot.event
async def on_reaction_add(reaction, user):
  # Only listen to reactions on own messages
  if reaction.message.author != bot.user:
    return

  PLAYER_USERNAME = user.global_name
  MESSAGE_ID = reaction.message.id
  if PLAYER_USERNAME == None:
    return

  print(reaction.emoji + " from: " + PLAYER_USERNAME)

  if not session_manager.is_valid_user_input(PLAYER_USERNAME, MESSAGE_ID):
    await reaction.remove(user)
    return

  await session_manager.enter_player_input(PLAYER_USERNAME, reaction.emoji)
  await reaction.remove(user)



#  for i in test_events:
#    if i[0].id == reaction.message.id and username == i[1]:
#      curr_content = i[0].content
#
#      edited_message = None
#      action = None
#      match(reaction.emoji):
#        case "◀️":
#          action = game.PlayerAction.REEL_IN
#        case "⏺":
#          action = game.PlayerAction.HOLD
#        case "▶️":
#          action = game.PlayerAction.SLACK
#      if action == None:
#        await reaction.remove(user)
#        return
#      current_state = game.take_fishing_action(i[0].id, action)
#      if current_state == None:
#        await reaction.remove(user)
#        return
#      new_content = game_state_to_view(current_state)
#
#      edited_message = await i[0].edit(content=new_content)
#
#      await reaction.remove(user)
#      test_events.remove(i)
#      test_events.append([edited_message, i[1]])
#
#
#DEFAULT_LINE_LENGTH = 20
#def game_state_to_view(state):
#  state_string = "🎣"
#  # Fish line
#  line_length = math.floor(state["length"] / state["max_length"] * DEFAULT_LINE_LENGTH)
#  for i in range(0, line_length):
#    state_string += "-"  
#  state_string += "🐟"
#  if state["length"] == 0:
#    state_string += " You caught it!"
#
#  # Line length
#  line_length = math.floor(state["length"] / state["max_length"] * DEFAULT_LINE_LENGTH)
#  state_string += "\n`Line Length   |"
#  for i in range(0, DEFAULT_LINE_LENGTH - line_length):
#    state_string += "-"  
#  for i in range(0, line_length):
#    state_string += " "  
#  state_string += "|`"
#  if state["length"] == state["max_length"]:
#    state_string += " No more slack!"
#
#  # Tension bar
#  line_length = math.floor(state["tension"] / state["max_tension"] * DEFAULT_LINE_LENGTH)
#  state_string += "\n`Tension Gauge |"
#  for i in range(0, line_length):
#    state_string += "="  
#  for i in range(0, DEFAULT_LINE_LENGTH - line_length):
#    state_string += " "  
#  if state["tension"] > state["max_tension"]:
#    state_string += "` Line broke! It got away!"
#  else:
#    state_string += "|`"
#
#  if len(state["fish_action_history"]) > 1:
#    state_string += "\nFish last action: " + str(state["fish_action_history"][-2])
#  else:
#    state_string += "\nFish last action: None"
#    
## Production
#  state_string += """
#◀️ Reel in ⏺ Hold ▶️ Slack
#""".format(**state)
#
## Testing
##  state_string += """
##Fish next action: {fish_action}
##Fish stamina: {stamina}/{max_stamina}
##◀️ Reel in ⏺ Hold ▶️ Slack
##""".format(**state)
#  return state_string


####################
# starting the bot #
####################
password_file = open("super_secret_pw", "r")
bot_token = password_file.read()
password_file.close()

logger = logging.getLogger(__name__)
logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.ERROR)
try:
  bot.run(bot_token)
except Exception as err:
  logger.error(f"Unexpected {err=}, {type(err)=}")


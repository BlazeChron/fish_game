#bot imports
import discord

# error logging
import logging
import traceback

import datetime

import setproctitle

import session_manager

# Temporary test db
import fish_db
fish_db.test_table()

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

  player_session = session_manager.get_session(PLAYER_USERNAME)
  if player_session == None or not player_session.get_message_id() == MESSAGE_ID:
    await reaction.remove(user)
    return
  
  await player_session.enter_player_input(reaction.emoji)
  await reaction.remove(user)

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


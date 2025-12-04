# bot imports
import discord

# error logging
import logging
import traceback

import datetime

import setproctitle

setproctitle.setproctitle("disc_fish_game")

bot = discord.Bot()

@bot.event
async def on_ready():
  print(f'Logged on as {bot.user}')

test_events = []

@bot.slash_command()
async def start(ctx: discord.ApplicationContext):
  interaction = await ctx.send_response("test")
  og_response = await interaction.original_response()
  await og_response.add_reaction("🗿")
  test_events.append(og_response)

  #await ctx.followup.send("test interaction")

@bot.event
async def on_raw_reaction_add(payload):
  if payload.event_type != "REACTION_ADD":
    return
  reaction = payload.emoji
  user = payload.member
  print(reaction)
  print(user)
  for i in test_events:
    if i.id == payload.message_id:
      curr_content = i.content
      print(curr_content)
      edited_message = None
      if curr_content.isnumeric():
        new_content = str(int(curr_content) + 1)
        edited_message = await i.edit(content=new_content)
      else:
        print("changing 0")
        edited_message = await i.edit(content="0")
      test_events.remove(i)
      test_events.append(edited_message)


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


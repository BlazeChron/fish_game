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

@bot.slash_command()
async def start(ctx: discord.ApplicationContext):
  await ctx.respond("start")

password_file = open("super_secret_pw", "r")
bot_token = password_file.read()
password_file.close()

logger = logging.getLogger(__name__)
logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.ERROR)
try:
  bot.run(bot_token)
except Exception as err:
  logger.error(f"Unexpected {err=}, {type(err)=}")


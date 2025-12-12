# Handles output to discord based on Session details
from enum import Enum
from scene.main_menu_scene import TestPlayerAction 

import discord_input_adapter as dia

import game_state_string_adapter as gssa

async def scene_to_output(scene, session):
  game_state = scene.get_game_state()
  # Handle scene
  new_content = gssa.state_to_string(game_state)
  await session.edit_message(new_content)

  # Handle new inputs
  # TODO Probably could use Sets instead

  # Converts the required inputs in a dic, with exist in message flags set to 0
  required_inputs = scene.get_required_inputs()
  converted_inputs = {}
  for ri in required_inputs:
    converted_inputs[dia.convert_game_to_discord(ri)] = 0

  # Iterates over each reaction in the message If it exists, flags it as 1.
  # Otherwise, it removes the reaction
  current_reactions = session.get_reactions()
  for reaction in current_reactions:
    emoji = reaction.emoji
    if not emoji in converted_inputs:
      await reaction.clear()
    else:
      converted_inputs[emoji] = 1

  # Afterwards, the remaining required reactions if flag is 0,
  # add the new reaction
  for emoji in converted_inputs.keys():
    if converted_inputs[emoji] == 0:
      await session.add_reaction(emoji)

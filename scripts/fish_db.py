# Interface for accessing database

# Temporary database for testing
temp_db = {}


def save_file_exists(PLAYER_USERNAME):
  return PLAYER_USERNAME in temp_db

def get_save_file(PLAYER_USERNAME):
  return temp_db[PLAYER_USERNAME]

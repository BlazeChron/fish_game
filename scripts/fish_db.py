# Interface for accessing database
import psycopg

# Environment variables
import os
from dotenv import load_dotenv
import db_scripts.db_setup

def save_file_exists(PLAYER_USERNAME):
  load_dotenv()
  username_exists_cursor = psycopg.connect(os.getenv("DB_STRING")).execute("""
    SELECT 1
    FROM users
    WHERE username = (%s);
  """, (PLAYER_USERNAME,))

  return username_exists_cursor.fetchone() != None

def get_save_file(PLAYER_USERNAME):
  load_dotenv()
  money_cursor = psycopg.connect(os.getenv("DB_STRING")).execute("""
    SELECT money
    FROM users
    WHERE username = (%s);
  """, (PLAYER_USERNAME,))
  money = money_cursor.fetchone()[0]
  
  return {"money": money}

def create_save_file(PLAYER_USERNAME):
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    conn.execute("""
    INSERT INTO users (username, money)
    VALUES (%s, %s);
  """, (PLAYER_USERNAME, 0))

def update_money(updated_amount, PLAYER_USERNAME):
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    conn.execute("""
      UPDATE users
      SET money = (%s)
      WHERE username = (%s);
    """, (updated_amount, PLAYER_USERNAME))

def reset_db():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
      cur.execute("DROP table IF EXISTS user_fish")
      cur.execute("DROP table IF EXISTS test")
      cur.execute("DROP table IF EXISTS users")
      cur.execute("""
        CREATE TABLE users (
          id serial PRIMARY KEY,
          username text UNIQUE,
          money integer
          )
      """)
      conn.commit()
  db_scripts.db_setup.create_user_fish()


def create_fishes():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
      cur.execute("DROP table IF EXISTS fish_types")
      cur.execute("""
        CREATE TABLE fish_types (
          id serial PRIMARY KEY,
          fish_name text UNIQUE,
          )
      """)
      conn.commit()

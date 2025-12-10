# Interface for accessing database
import psycopg

# Environment variables
import os
from dotenv import load_dotenv

def save_file_exists(PLAYER_USERNAME):
  username_exists_cursor = psycopg.connect(os.getenv("DB_STRING")).execute("""
    SELECT 1
    FROM users
    WHERE username = (%s);
  """, (PLAYER_USERNAME,))

  return username_exists_cursor.fetchone() != None

def get_save_file(PLAYER_USERNAME):
  money_cursor = psycopg.connect(os.getenv("DB_STRING")).execute("""
    SELECT money
    FROM users
    WHERE username = (%s);
  """, (PLAYER_USERNAME,))
  money = money_cursor.fetchone()[0]
  
  return {"money": money}

def create_save_file(PLAYER_USERNAME):
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    conn.execute("""
    INSERT INTO users (username, money)
    VALUES (%s, %s);
  """, (PLAYER_USERNAME, 0))

def update_money(updated_amount, PLAYER_USERNAME):
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    conn.execute("""
      UPDATE users
      SET money = (%s)
      WHERE username = (%s);
    """, (updated_amount, PLAYER_USERNAME))

def test_table():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
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

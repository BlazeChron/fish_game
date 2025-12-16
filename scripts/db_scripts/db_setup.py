# Interface for accessing database
import psycopg

# Environment variables
import os
from dotenv import load_dotenv

import random
import scipy.stats

# id serial PRIMARY KEY,
# type text UNIQUE,
# color text,
# size_mean integer, in /100 of cm (convert to cm by /100)
# size_variance integer,
# appearance_weight integer

def create_fish_types():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
      cur.execute("DROP table IF EXISTS fish_types")
      cur.execute("""
        CREATE TABLE fish_types (
          id serial PRIMARY KEY,
          type text UNIQUE,
          color text,
          size_mean integer,
          size_variance integer,
          appearance_weight integer
          )
      """)
      conn.commit()

def delete_fish_types():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
      cur.execute("DROP table IF EXISTS fish_types")
      conn.commit()

fish_types = [["A fish", "red", 1000, 100, 10],
              ["B fish", "blue", 1000, 100, 5],
              ["C fish", "green", 1000, 100, 3],
              ["D fish", "yellow", 1000, 100, 2],
              ["E fish", "purple", 1000, 100, 1],
              ["F fish", "orange", 1000, 100, 6],
              ]

def add_fish_types():
  load_dotenv()
  with psycopg.connect(os.getenv("DB_STRING")) as conn:
    with conn.cursor() as cur:
      cur.executemany("""
        INSERT INTO fish_types (type, color, size_mean, size_variance, appearance_weight) 
        VALUES (%s, %s, %s, %s, %s)
      """, [(x[0], x[1], x[2], x[3], x[4]) for x in fish_types])
      conn.commit()

def create_fish():
  load_dotenv()
  cur = psycopg.connect(os.getenv("DB_STRING")).execute("SELECT * FROM fish_types").fetchall()

  total = 0
  for record in cur:
    total += record[5]
  roll_type = random.randint(0, total)

  curr_total = 0
  chosen_record = None
  for record in cur:
    curr_total += record[5]
    if roll_type <= curr_total:
      chosen_record = record
      break

  # Rolling number between 0 to 1 to determine fish size based on norm distribution
  roll_size = random.random()
  roll_string = "{:.2f}%".format(roll_size * 100)
  string_sizes = [[0.05, "Mini Crown"], [0.10, "XS"], [0.30,"S"], [0.70, "M"], [0.90, "L"], [0.95, "XL"], [1, "Large Crown"]]
  size_value = ""
  for entry in string_sizes:
    if roll_size <= entry[0]:
      size_value = entry[1]
      break
  size = scipy.stats.norm.ppf(roll_size, loc=chosen_record[3], scale=chosen_record[4])
  print("Size: {:.2f}cm".format(size / 100) + " " + size_value + " " + roll_string)

# Testing purposes
def a():
  create_fish_types()
  add_fish_types()

def b():
  for i in range(30):
    create_fish()

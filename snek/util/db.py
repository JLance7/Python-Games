import datetime
import sqlite3
from .my_logger import logger

conn = sqlite3.connect('.high_scores.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores(
             high_score INT PRIMARY KEY NOT NULL,
             date DATE NOT NULL
            );
             ''')


def try_insert_score(score: int):
  date = datetime.date.today()

  result = cursor.execute('SELECT MAX(high_score) FROM scores')
  result = result.fetchone()
  high_score = result[0]
  if high_score != None:
    logger.info(f'high score {high_score} found')
    if high_score < score:
      print(f'inerting new high score {score}')
      cursor.execute('INSERT INTO scores (high_score, date) VALUES (?, ?)', (score, date))
      conn.commit()
  else:
    logger.info(f'no high score yet, isnerting new score {score}')
    cursor.execute('INSERT INTO scores (high_score, date) VALUES (?, ?)', (score, date))
    conn.commit()


def get_high_score(score):
  result = cursor.execute('SELECT MAX(high_score) FROM scores')
  try:
    result = result.fetchone()[0]
    return result
  except:
    return score


if __name__ == "__main__":
  try_insert_score(1)
  # print(get_high_score())
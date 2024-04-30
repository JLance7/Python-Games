import random
from constants import *

def get_random_player_pos():
  x = random.randrange(0, WIDTH)//PLAYER_WIDTH * PLAYER_WIDTH
  y = random.randrange(0, WIDTH)//PLAYER_WIDTH * PLAYER_WIDTH
  return x, y
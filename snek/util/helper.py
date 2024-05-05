import random
from constants import *

def get_random_player_pos(cell_subtractor=0):
  random_x = (random.randrange(0, WIDTH-PLAYER_WIDTH)//PLAYER_WIDTH)
  random_y = (random.randrange(0, WIDTH-PLAYER_WIDTH)//PLAYER_WIDTH)
  if cell_subtractor != 0 and random_x > 10: # since snake starts out going to right, make sure it isn't up against the right screen
    x = (random_x - cell_subtractor) * PLAYER_WIDTH
    y = random_y * PLAYER_WIDTH
  else:
    x = random_x * PLAYER_WIDTH
    y = random_y * PLAYER_WIDTH

  return x, y
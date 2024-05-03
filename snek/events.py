import pygame, sys
from pygame import USEREVENT
from gaming import food_pos_x, food_pos_y
from util.helper import get_random_player_pos
from constants import PLAYER_WIDTH
from util.logger import logger

# Events
COLLISION = USEREVENT + 1
FOOD_ACQUIRED = USEREVENT + 2


def check_events(food_pos_x, food_pos_y, snake, direction):
  from gaming import Direction

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

    if event.type == COLLISION:
      logger.info('collision')
    #  pygame.quit()
    #  sys.exit()  
   
  #  if event.type == FOOD_ACQUIRED:
  #    new_food_pos_x, new_food_pos_y = get_random_player_pos()
  #    food_pos_x = new_food_pos_x
  #    food_pos_y = new_food_pos_y
  #    if direction == Direction.UP:
  #     snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y'] + PLAYER_WIDTH})
  #    elif direction == Direction.DOWN:
  #     snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y'] - PLAYER_WIDTH})
  #    elif direction == Direction.LEFT:
  #     snake.append({'x': snake[-1]['x'] + PLAYER_WIDTH, 'y': snake[-1]['y']})
  #    elif direction == Direction.RIGHT:
  #     snake.append({'x': snake[-1]['x'] - PLAYER_WIDTH, 'y': snake[-1]['y']})

    if event.type == FOOD_ACQUIRED:
      new_food_pos_x, new_food_pos_y = get_random_player_pos()
      food_pos_x = new_food_pos_x
      food_pos_y = new_food_pos_y
      if direction == Direction.UP:
        snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y'] + PLAYER_WIDTH})
      elif direction == Direction.DOWN:
        snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y'] - PLAYER_WIDTH})
      elif direction == Direction.LEFT:
        snake.append({'x': snake[-1]['x'] + PLAYER_WIDTH, 'y': snake[-1]['y']})
      elif direction == Direction.RIGHT:
        snake.append({'x': snake[-1]['x'] - PLAYER_WIDTH, 'y': snake[-1]['y']})
      logger.info('food acquired')   
  
  return food_pos_x, food_pos_y

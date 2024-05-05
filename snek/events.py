import pygame, sys
from pygame import USEREVENT
from util.helper import get_random_player_pos
from util.logger import logger
from typing import List
from my_types import Snake
from drawing import game_over_screen

# Events
COLLISION = USEREVENT + 1
FOOD_ACQUIRED = USEREVENT + 2

def check_events(food_pos_x: int, food_pos_y: int, snake: List[Snake], direction):
  from my_types import Direction
  from gaming import get_direction, handle_movement

  for event in pygame.event.get():
    # key pressed
    if event.type == pygame.KEYDOWN:
      direction = get_direction(event.key, direction)
      
      if event.key == pygame.K_UP and direction != Direction.DOWN:
        direction = Direction.UP
      elif event.key == pygame.K_DOWN and direction != Direction.UP:
        direction = Direction.DOWN
      elif event.key == pygame.K_RIGHT and direction != Direction.LEFT:
        direction = Direction.RIGHT
      elif event.key == pygame.K_LEFT and direction != Direction.RIGHT:
        direction = Direction.LEFT

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

    if event.type == COLLISION:
      logger.info('collision')
      # game_over_screen(len(snake)) 

    if event.type == FOOD_ACQUIRED:
      while True:
        new_food_pos_x, new_food_pos_y = get_random_player_pos()
        if new_food_pos_x != snake[0].x: break

      food_pos_x = new_food_pos_x
      food_pos_y = new_food_pos_y
      # if direction == Direction.UP:
      #   snake.append({'x': last_snake_x_pos, 'y': last_snake_y_pos + PLAYER_WIDTH})
      # elif direction == Direction.DOWN:
      #   snake.append({'x': last_snake_x_pos, 'y': last_snake_y_pos - PLAYER_WIDTH})
      # elif direction == Direction.LEFT:
      #   snake.append({'x': last_snake_x_pos + PLAYER_WIDTH, 'y': last_snake_y_pos})
      # elif direction == Direction.RIGHT:
      #   snake.append({'x': last_snake_x_pos - PLAYER_WIDTH, 'y': last_snake_y_pos})
      # logger.info('food acquired')
  return food_pos_x, food_pos_y, direction

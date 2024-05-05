import pygame, sys
from pygame import USEREVENT
from util.helper import get_random_player_pos
from util.my_logger import logger
from typing import List
from my_types import Snake, Direction
from drawing import game_over_screen, win_screen

# Events
COLLISION = USEREVENT + 1
FOOD_ACQUIRED = USEREVENT + 2

def check_events(food_pos_x: int, food_pos_y: int, snake: List[Snake], direction: Direction):
  from gaming import get_new_direction, handle_movement
  new_direction = direction

  for event in pygame.event.get():
    # key pressed
    if event.type == pygame.KEYDOWN:      
      if event.key == pygame.K_UP:
        new_direction = Direction.UP
      elif event.key == pygame.K_DOWN:
        new_direction = Direction.DOWN
      elif event.key == pygame.K_RIGHT:
        new_direction = Direction.RIGHT
      elif event.key == pygame.K_LEFT:
        new_direction = Direction.LEFT
      else:
        new_direction = direction
      

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

    if event.type == COLLISION:
      # pass
      # logger.info('collision')
      game_over_screen(len(snake)) 

    if event.type == FOOD_ACQUIRED:
      if (len(snake) == 255): win_screen(score=len(snake))
      while True:
        print('here')
        new_food_pos_x, new_food_pos_y = get_random_player_pos()
        print('new_food_pos_x', new_food_pos_x)
        valid = True
        for segment in snake:
          if new_food_pos_x == segment.x and new_food_pos_y == segment.y: 
            valid = False
        if valid: break

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
  direction = get_new_direction(direction, new_direction)
  return food_pos_x, food_pos_y, direction

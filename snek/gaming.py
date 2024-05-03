from enum import Enum
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from constants import *
from colors import *
from drawing import draw_screen
from util.helper import get_random_player_pos


class Direction(Enum):
  UP = 0
  DOWN = 1
  RIGHT = 2
  LEFT = 3

direction = Direction.RIGHT
food_pos_x, food_pos_y = 0, 0
from events import check_events, COLLISION, FOOD_ACQUIRED

def main():
  global direction, food_pos_x, food_pos_y
  pygame.init()
  pygame.font.init()
  INFO = pygame.display.Info()
  pygame.display.set_caption("Snake")
  clock = pygame.time.Clock()
  player_pos_x, player_pos_y = get_random_player_pos()
  while True:
    food_pos_x, food_pos_y = get_random_player_pos()
    if food_pos_x != player_pos_x: break
  time_elapsed_since_last_action = 0
  run = True
  snake = []
  snake.append({
    'x': player_pos_x, 
    'y': player_pos_y
  })

  while run:
    time = clock.tick(FPS)
    time_elapsed_since_last_action += time

    keys_pressed = pygame.key.get_pressed()     
    direction = get_direction(keys_pressed, direction)
    if time_elapsed_since_last_action > 150:  
      handle_movement(direction, snake)
      time_elapsed_since_last_action = 0

    draw_screen(snake, food_pos_x, food_pos_y)
    check_player_and_food(snake, food_pos_x, food_pos_y)
    food_pos_x, food_pos_y = check_events(food_pos_x, food_pos_y, snake, direction)


def get_direction(keys_pressed, direction):
  if keys_pressed[pygame.K_UP] and direction != Direction.DOWN:
    direction = Direction.UP
  elif keys_pressed[pygame.K_DOWN] and direction != Direction.UP:
    direction = Direction.DOWN
  elif keys_pressed[pygame.K_RIGHT] and direction != Direction.LEFT:
    direction = Direction.RIGHT
  elif keys_pressed[pygame.K_LEFT] and direction != Direction.RIGHT:
    direction = Direction.LEFT
  # print(direction)
  return direction


def handle_movement(direction, snake):
  # set segment cords to segment cords ahead of it in list, if first increment/decremnt cords based on direction
  for i in range(len(snake)-1, -1, -1):
    if i != 0:
      snake[i]['x'] = snake[i-1]['x']
      snake[i]['y'] = snake[i-1]['y']
    else:
      if direction == direction.UP:
        snake[i]['y'] -= PLAYER_WIDTH
      elif direction == direction.DOWN:
        snake[i]['y'] += PLAYER_WIDTH
      elif direction == direction.RIGHT:
        snake[i]['x'] += PLAYER_WIDTH
      elif direction == direction.LEFT:
        snake[i]['x'] -= PLAYER_WIDTH
  # for i in range(len(snake)):
  #   if i == 0:
  #     if direction == direction.UP:
  #       snake[i]['y'] -= PLAYER_WIDTH
  #     elif direction == direction.DOWN:
  #       snake[i]['y'] += PLAYER_WIDTH
  #     elif direction == direction.RIGHT:
  #       snake[i]['x'] += PLAYER_WIDTH
  #     elif direction == direction.LEFT:
  #       snake[i]['x'] -= PLAYER_WIDTH
  #   elif i == 1:
  #     snake[i]['x'] = original_head_x
  #     if direction == direction.UP:
  #       snake[i]['y'] = snake[i-1]['y'] + PLAYER_WIDTH
  #     elif direction == direction.DOWN:
  #       snake[i]['y'] = snake[i-1]['y'] - PLAYER_WIDTH
  #     elif direction == direction.RIGHT:
  #       snake[i]['x'] = snake[i-1]['x'] - PLAYER_WIDTH
  #     elif direction == direction.LEFT:
  #       snake[i]['x'] = snake[i-1]['x'] + PLAYER_WIDTH


def check_player_and_food(snake, food_pos_x, food_pos_y):
  if snake[0]['x'] < 0:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0]['x'] > WIDTH:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0]['y'] < 0:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0]['y'] > HEIGHT:
    pygame.event.post(pygame.event.Event(COLLISION))

  if snake[0]['x'] == food_pos_x and snake[0]['y'] == food_pos_y:
    pygame.event.post(pygame.event.Event(FOOD_ACQUIRED))


if __name__ == "__main__":
  main()
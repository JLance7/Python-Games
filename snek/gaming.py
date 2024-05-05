from enum import Enum
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from constants import *
from colors import *
from drawing import draw_screen
from util.helper import get_random_player_pos
from util.my_logger import logger
from my_types import Direction, Snake
from events import check_events, COLLISION, FOOD_ACQUIRED


def main():
  direction = Direction.RIGHT
  food_pos_x, food_pos_y = 0, 0
  pygame.init()
  pygame.font.init()
  INFO = pygame.display.Info()
  pygame.display.set_caption("Snake")
  clock = pygame.time.Clock()
  player_pos_x, player_pos_y = get_random_player_pos(5)
  while True:
    food_pos_x, food_pos_y = get_random_player_pos()
    if food_pos_x != player_pos_x: break
  time_elapsed_since_last_action = 0
  run = True
  snake = []
  snake.append(Snake(player_pos_x, player_pos_y))

  while run:
    time = clock.tick(FPS)
    time_elapsed_since_last_action += time
    food_pos_x, food_pos_y, direction = check_events(food_pos_x, food_pos_y, snake, direction)

    # keys_pressed = pygame.key.get_pressed()     
    if time_elapsed_since_last_action > 150:  
      handle_movement(direction, snake, food_pos_x, food_pos_y)
      time_elapsed_since_last_action = 0
    check_collision(snake)
    draw_screen(snake, food_pos_x, food_pos_y, len(snake))


def get_new_direction(direction, new_direction):
  # if keys_pressed[pygame.K_UP] and direction != Direction.DOWN:
#     direction = Direction.UP
#   elif keys_pressed[pygame.K_DOWN] and direction != Direction.UP:
#     direction = Direction.DOWN
#   elif keys_pressed[pygame.K_RIGHT] and direction != Direction.LEFT:
#     direction = Direction.RIGHT
#   elif keys_pressed[pygame.K_LEFT] and direction != Direction.RIGHT:
#     direction = Direction.LEFT
#   # print(direction)
#   return direction

  if new_direction == Direction.UP and direction != Direction.DOWN:
    direction = new_direction
  elif new_direction == Direction.DOWN and direction != Direction.UP:
    direction = new_direction
  elif new_direction == Direction.LEFT and direction != Direction.RIGHT:
    direction = new_direction
  elif new_direction == Direction.RIGHT and direction != Direction.LEFT:
    direction = new_direction
  # print('get_new_direction:', direction)
  return direction


def handle_movement(direction, snake, food_pos_x, food_pos_y):
  # for i in range(len(snake)-1, -1, -1):
  #   if i != 0:
  #     snake[i]['x'] = snake[i-1]['x']
  #     snake[i]['y'] = snake[i-1]['y']
  #   else:
  #     if direction == direction.UP:
  #       snake[i]['y'] -= PLAYER_WIDTH
  #     elif direction == direction.DOWN:
  #       snake[i]['y'] += PLAYER_WIDTH
  #     elif direction == direction.RIGHT:
  #       snake[i]['x'] += PLAYER_WIDTH
  #     elif direction == direction.LEFT:
  #       snake[i]['x'] -= PLAYER_WIDTH
  new_snake_pos = Snake(snake[0].x, snake[0].y)
  # print('handle_movement_direction', direction)
  if direction == direction.UP:
    new_snake_pos.y -= PLAYER_WIDTH
  elif direction == direction.DOWN:
    new_snake_pos.y += PLAYER_WIDTH
  elif direction == direction.RIGHT:
     new_snake_pos.x += PLAYER_WIDTH
  elif direction == direction.LEFT:
     new_snake_pos.x -= PLAYER_WIDTH
  snake.insert(0, new_snake_pos)
  if check_food(snake, food_pos_x, food_pos_y):
    pass
  else:
    snake.pop()


def check_collision(snake):
  if snake[0].x < 0:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0].x > WIDTH:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0].y < 0:
    pygame.event.post(pygame.event.Event(COLLISION))
  if snake[0].y > HEIGHT:
    pygame.event.post(pygame.event.Event(COLLISION))
  
  for segment in snake[1:]:
    if snake[0].x == segment.x and snake[0].y == segment.y:
      pygame.event.post(pygame.event.Event(COLLISION))


def check_food(snake, food_pos_x, food_pos_y):
  """Returns true if snake collides with food and sends event to create new food location"""
  if snake[0].x == food_pos_x and snake[0].y == food_pos_y:
    pygame.event.post(pygame.event.Event(FOOD_ACQUIRED))
    return True
  return False


if __name__ == "__main__":
  main()
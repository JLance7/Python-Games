import pygame
from constants import *
from colors import *
from typing import List


def draw_screen(snake: List[dict], food_pos_x: int, food_pos_y: int):
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  draw_lines()
  # food
  draw_cube(food_pos_x, food_pos_y, RED)
  # snake
  for segment in snake:
    draw_cube(segment['x'], segment['y'], GREEN)
  pygame.display.update()


# Rect (left, top, width, height)
def draw_lines():
  # draw vertical lines
  for x in range(0, WIDTH, 40):
    # print('x:', x) 
    line = pygame.Rect(x - LINE_WIDTH, 0, LINE_WIDTH, HEIGHT)
    pygame.draw.rect(WIN, WHITE, line)
  
  # draw horizontal lines
  for y in range(0, HEIGHT, 40):
    # print('y: ', y)
    line = pygame.Rect(0, y - LINE_WIDTH, WIDTH, LINE_WIDTH)
    pygame.draw.rect(WIN, WHITE, line)


def draw_cube(pos_x: int, pos_y: int, color):
  player = pygame.Rect(pos_x, pos_y, PLAYER_WIDTH, PLAYER_WIDTH)
  pygame.draw.rect(WIN, color, player)

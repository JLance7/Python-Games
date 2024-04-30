import pygame
from constants import *
from colors import *


def draw_screen(player_pos_x: int, player_pos_y: int):
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  draw_lines()
  draw_snake(player_pos_x, player_pos_y)
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


def draw_snake(pos_x: int, pos_y: int):
  player = pygame.Rect(pos_x, pos_y, PLAYER_WIDTH, PLAYER_WIDTH)
  pygame.draw.rect(WIN, GREEN, player)
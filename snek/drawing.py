import pygame
from constants import *
from colors import *
from typing import List
from my_types import Snake


def draw_screen(snake: List[Snake], food_pos_x: int, food_pos_y: int, score: int):
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  draw_lines()
  # food
  draw_cube(food_pos_x, food_pos_y, RED)
  # snake
  for segment in snake:
    draw_cube(segment.x, segment.y, GREEN)
  show_score(score)
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


def game_over_screen(score: int):
  my_font = pygame.font.SysFont('Bahnschrift', 50)
  game_over_text = my_font.render('Game over', True, (255, 255, 255))
    
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  WIN.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))
  pygame.display.flip()
    
  pygame.time.delay(2000)
  pygame.quit()
  quit()


def show_score(score):
  my_font = pygame.font.SysFont('Bahnschrift', 32)
  score_text = my_font.render(f'Score: {score}', True, GREEN)
  WIN.blit(score_text, (score_text.get_width()//9, 7))
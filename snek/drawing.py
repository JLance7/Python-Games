import pygame, sys
from constants import *
from colors import *
from typing import List
from my_types import Snake
from util.db import try_insert_score, get_high_score


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
  print('score', score)
  from gaming import main

  try_insert_score(score)
  new_score: int = get_high_score(score)

  my_font = pygame.font.SysFont('Bahnschrift', 50)
  game_over_text = my_font.render('Game over', True, WHITE)
    
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  WIN.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))

  my_font2 = pygame.font.SysFont('Bahnschrift', 40)
  score_text = my_font2.render(f'Your Score: {score}', True, WHITE)
  WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//4 + 50))

  high_score_text = my_font2.render(f'High Score: {new_score}', True, WHITE)
  WIN.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//4 + 80))



  play_again_text = my_font2.render('Press \'enter\' to play again or \'esc\' to quit', True, WHITE)
  WIN.blit(play_again_text, (WIDTH//2 - play_again_text.get_width()//2, HEIGHT//4 + 120))
  pygame.display.flip()
  run = True
  clock = pygame.time.Clock()
  while run:
      clock.tick(FPS)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
              run = False
              main()
            elif event.key == pygame.K_ESCAPE:
              run = False
              pygame.quit()
              sys.exit()


def show_score(score):
  my_font = pygame.font.SysFont('Bahnschrift', 32)
  score_text = my_font.render(f'Score: {score}', True, GREEN)
  WIN.blit(score_text, (score_text.get_width()//9, 7))


def win_screen(score):
  try_insert_score(score)
  my_font = pygame.font.SysFont('Bahnschrift', 50)
  game_over_text = my_font.render('You Win!', True, WHITE)
    
  pygame.draw.rect(WIN, BLACK, BACKGROUND)
  WIN.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4))
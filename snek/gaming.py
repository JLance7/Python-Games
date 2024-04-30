import pygame, random
from constants import *
from colors import *
from events import *
from drawing import draw_screen
from util.helper import get_random_player_pos


def main():
  pygame.init()
  pygame.font.init()
  INFO = pygame.display.Info()
  pygame.display.set_caption("Snake")
  clock = pygame.time.Clock()
  run = True
  player_pos_x, player_pos_y = get_random_player_pos()

  while run:
    clock.tick(FPS)
    check_events()
    keys_pressed = pygame.key.get_pressed()        
    handle_movement(keys_pressed)
    draw_screen(player_pos_x, player_pos_y)


def handle_movement(keys_pressed):
  if keys_pressed[pygame.K_w]:
    pass
  if keys_pressed[pygame.K_DOWN]:
    pass
  if keys_pressed[pygame.K_RIGHT]:
    pass
  if keys_pressed[pygame.K_LEFT]:
    pass


if __name__ == "__main__":
  main()
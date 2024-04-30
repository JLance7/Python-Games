import pygame, sys
from pygame import USEREVENT

# Events
FOOD_ACQUIRED = USEREVENT + 1


def check_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        sys.exit() 
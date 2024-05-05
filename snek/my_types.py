from enum import Enum


class Direction(Enum):
  UP = 0
  DOWN = 1
  RIGHT = 2
  LEFT = 3


class Snake():
  x: int
  y: int

  def __init__(self, x, y):
    self.x = x
    self.y = y
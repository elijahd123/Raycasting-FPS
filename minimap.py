from pygame.draw import rect
from pygame import Rect
from math import sqrt


class Minimap:
    def __init__(self, border_colour, gap: int = 25, scale: int = 50, width: int = 200, height: int = 200):
        self.border_colour = border_colour
        self.x = gap
        self.y = gap
        self.scale = scale
        self.width = width
        self.height = height
        self.max_depth = int(sqrt((self.width * self.scale) ** 2 + (self.height * self.scale) ** 2))

    def draw_border(self, window):
        rect(window, self.border_colour, Rect(self.x, self.y, self.width, self.height))

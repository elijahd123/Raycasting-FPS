from pygame.draw import line, rect
from pygame import Rect


class Realm:
    def __init__(self, columns: int, width: int, height: int):
        self.columns = columns
        self.width = width
        self.height = height
        self.column_width = self.width / self.columns

    def draw_background(self, window, sky_colour, floor_colour):
        rect(window, sky_colour, Rect(0, 0, self.width, self.height / 2))
        rect(window, floor_colour, Rect(0, self.height / 2, self.width, self.height))

    def calculate_and_draw_column(self, window, distance, column):
        colour = [0 for _ in range(3)]
        height = distance
        self.draw_column(window, colour, column, height)

    def draw_column(self, window, colour, column: int, height: int):
        y_gap = (self.height - height) / 2
        x = (column + 0.5) * self.column_width
        line(window, colour, (x, y_gap), (x, self.height - y_gap), int(self.column_width))

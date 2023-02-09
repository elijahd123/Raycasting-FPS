from pygame.draw import rect, polygon
from pygame import Rect
from math import sqrt, hypot, atan2, sin, cos


class Minimap:
    def __init__(self, border_colour, gap: int = 25, width: int = 200, height: int = 200):
        self.border_colour = border_colour
        self.x = gap
        self.y = gap
        self.width = width
        self.height = height
        self.max_depth = int(sqrt(self.width ** 2 + self.height ** 2))

    def draw_border(self, window):
        rect(window, self.border_colour, Rect(self.x, self.y, self.width, self.height))

    def draw_tile(self, window, x: int, y: int, width_length: int, height_length: int, colour):

        tile_width, tile_height = self.width // width_length, self.height // height_length

        rect(window, colour, Rect(self.x + (x * tile_width), self.y + (y * tile_height), tile_width, tile_height))

    def draw_player(self, window, player_x: int, player_y: int, player_angle: float, relative_points, colour):
        points = []
        for point in relative_points:
            x, y = point[0], point[1]

            dist = hypot(x, y)

            angle = atan2(y, x) + player_angle

            points.append([self.x + player_x + (dist * cos(angle)), self.y + player_y + (dist * sin(angle))])

        polygon(window, colour, points)

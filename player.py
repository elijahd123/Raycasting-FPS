from math import pi, sin, cos


class Player:
    def __init__(self, x: int, y: int, speed: int = 3, angle: float = pi):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.forward = True
        self.turn_angle = pi / 24
        self.relative_points = [[0, 10], [-6, -6], [0, -4], [6, -6]]

    def calculate_movement(self, forward: bool = False, left: bool = False, backward: bool = False, right: bool = False):
        if left:
            self.angle -= self.turn_angle

        if right:
            self.angle += self.turn_angle

        if forward:
            self.forward = True
            self.x += -sin(self.angle) * self.speed
            self.y += cos(self.angle) * self.speed

        if backward:
            self.forward = False
            self.x -= -sin(self.angle) * self.speed
            self.y -= cos(self.angle) * self.speed

    def collision_avoid(self):
        diff_x = -sin(self.angle) * self.speed
        diff_y = cos(self.angle) * self.speed
        if self.forward:
            self.x -= diff_x
            self.y -= diff_y
        else:
            self.x += diff_x
            self.y += diff_y

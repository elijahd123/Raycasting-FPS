from math import pi, sin, cos


class Player:
    def __init__(self, x: int, y: int, speed: int = 5, angle: float = pi):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.forward = True
        self.fov = pi / 3
        self.half_fov = self.fov / 2
        self.casted_rays = 128
        self.step_angle = self.fov / (self.casted_rays - 1)

    def calculate_movement(self, forward: bool = False, left: bool = False, backward: bool = False, right: bool = False):
        if left:
            self.angle -= self.step_angle

        if right:
            self.angle += self.step_angle

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

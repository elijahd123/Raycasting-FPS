from math import pi


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

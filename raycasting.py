from math import pi, cos
"""def cast_rays():
    start_angle = player_angle - half_fov

    for ray in range(casted_rays):
        for depth in range(max_depth):
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y + math.cos(start_angle) * depth

            target_map_x, target_map_y = int(target_x / two_d_block_width), int(target_y / two_d_block_height)

            block = two_d_area[target_map_y][target_map_x]
            if block == block_char:
                pygame.draw.rect(win, (40, 255, 40), pygame.Rect(target_map_x * two_d_block_width,
                                                                 target_map_y * two_d_block_height, two_d_block_width,
                                                                 two_d_block_height))

                pygame.draw.line(win, (255, 255, 0), (player_x, player_y), (target_x, target_y), 3)

                # wall shading
                colour = (255 / (1 + (depth ** 2) * 0.0001))

                # fix fisheye effect
                depth *= math.cos(player_angle - start_angle)

                # calculate wall height
                wall_height = 21000 / (depth + 0.0001)

                # draw 3d area
                pygame.draw.rect(win, (colour, colour, colour),
                                 pygame.Rect((width // 2) + ray * scale, (height // 2) - (wall_height // 2), scale,
                                             wall_height))

                break

        start_angle += step_angle"""


class RayCaster:
    def __init__(self, ray_count: int = 128):
        self.ray_count = ray_count
        self.fov = pi / 3
        self.half_fov = self.fov / 2
        self.step_angle = self.fov / (self.ray_count - 1)

    def cast(self, window, draw_func, player_angle):
        for ray_index in range(self.ray_count):
            angle = player_angle - self.half_fov + ray_index * self.step_angle



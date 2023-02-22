from math import pi, sqrt, cos, sin, tan


class RayCaster:
    def __init__(self, width: int, height: int, ray_count: int = 128):
        self.ray_count = ray_count
        self.fov = pi / 3
        self.half_fov = self.fov / 2
        self.step_angle = self.fov / (self.ray_count - 1)
        self.max_length = sqrt(width ** 2 + height ** 2)

    def cast(self, window, draw_func, player_angle, player_coords, width, height, max_depth, area, get_tile, block_char):
        angle = pi / 2 + player_angle - self.half_fov - self.step_angle
        ray_ends = []
        max_dist = sqrt((width ** 2) + (height ** 2))
        for ray_index in range(self.ray_count):
            angle += self.step_angle
            max_dist_point = (player_coords[0] + max_dist * cos(angle), player_coords[1] + max_dist * sin(angle))
            y_per_x = tan(angle)
            x_per_y = 1/y_per_x
            tot_y = 0
            tot_x = 0
            loop = 0
            while get_tile(area, (player_coords[0] + tot_x, player_coords[1] + tot_y)) != block_char or loop < 10:
                loop += 1
                if abs(tot_x + x_per_y) > abs(tot_y + y_per_x):
                    tot_y += y_per_x
                else: tot_x += x_per_y

            distance = sqrt((tot_x ** 2) + (tot_y ** 2))
            ray_ends.append((player_coords[0] + distance * cos(angle), player_coords[1] + distance * sin(angle)))
            # create ray and calc distance, and append end point to ray_ends
            draw_func(window, distance, ray_index)

        return ray_ends

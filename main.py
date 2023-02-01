from colours import Colours
from player import Player
from area import Area
from window import Window
from minimap import Minimap
import pygame
import math

area_constant = [
    "########",
    "#      #",
    "#      #",
    "#      #",
    "#  #   #",
    "#   #  #",
    "#      #",
    "########"
]

colours = Colours()
area = Area(area_constant)
window = Window()
minimap = Minimap()
player = Player((minimap.width * minimap.scale) // 2, (minimap.height * minimap.scale) // 2, speed=minimap.scale * 5)

# ray casting algorithm
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

# main loop
while window.run:
    # in-loop frame settings
    window.clock.tick(window.fps)
    window.frame = (window.frame + 1) % window.fps

    # adding the fps to the caption
    window.update_caption(f"Ray casting - {int(round(window.clock.get_fps()))} fps")

    # checking if the user has closed the window
    if pygame.event.get(pygame.QUIT):
        run = False
        continue

    # getting user input
    keys = pygame.key.get_pressed()

    # using user input
    if keys[pygame.K_a]:
        player.angle -= player.step_angle

    if keys[pygame.K_d]:
        player.angle += player.step_angle

    if keys[pygame.K_w]:
        player.forward = True
        player.x += -math.sin(player.angle) * player.speed
        player.y += math.cos(player.angle) * player.speed

    if keys[pygame.K_s]:
        player.forward = False
        player.x -= -math.sin(player.angle) * player.speed
        player.y -= math.cos(player.angle) * player.speed

    block = area.area[int((player.x * len(area.area[-1])) / (minimap.scale * minimap.width))][
        int((player.y * len(area.area)) / (minimap.scale * minimap.height))]

    if block == area.block_char:
        diff_x = -math.sin(player.angle) * player.speed
        diff_y = math.cos(player.angle) * player.speed
        if player.forward:
            player.x -= diff_x
            player.y -= diff_y
        else:
            player.x += diff_x
            player.y += diff_y

    window.window.fill(colours.black)

    # ray cast

    # draw area

    minimap.draw_border(window.window)

    # draw minimap

    pygame.display.update()

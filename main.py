import random

from colours import Colours
from player import Player
from area import Area
from window import Window
from minimap import Minimap
from realm import Realm
import pygame

area_constant = [
    "########",
    "#      #",
    "# ##   #",
    "#    # #",
    "#  #   #",
    "#   #  #",
    "##    ##",
    "########"
]

colours = Colours()
area = Area(area_constant)
window = Window()
minimap = Minimap(colours.back)
player = Player((minimap.width * minimap.scale) // 2, (minimap.height * minimap.scale) // 2, speed=minimap.scale * 3)
realm = Realm(player.casted_rays, window.width, window.height)

while window.run:
    # frame settings
    window.clock.tick(window.fps)
    window.frame = (window.frame + 1) % window.fps

    # adding the fps to the caption
    window.update_caption(f"Ray casting - {int(round(window.clock.get_fps()))} fps")

    # getting user input
    keys = pygame.key.get_pressed()

    # checking if the user has closed the window
    if pygame.event.get(pygame.QUIT) or keys[pygame.K_ESCAPE]:
        window.run = False
        continue

    # using user input
    player.calculate_movement(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d])

    block = area.area[
        int((player.y * len(area.area)) / (minimap.scale * minimap.height))
    ][
        int((player.x * len(area.area[-1])) / (minimap.scale * minimap.width))
    ]

    if block == area.block_char:
        player.collision_avoid()

    window.window.fill(colours.black)

    realm.draw_background(window.window, colours.sky, colours.back)

    # ray cast

    minimap.draw_border(window.window)

    for y in range(len(area.area)):
        for x in range(len(area.area[y])):
            if area.area[y][x] == area.block_char:
                minimap.draw_tile(window.window, x, y, len(area.area[y]), len(area.area), colours.block)

    minimap.draw_player(window.window, player.x // minimap.scale, player.y // minimap.scale, player.angle, player.relative_points, colours.white)

    pygame.display.update()

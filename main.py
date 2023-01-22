import pygame
import math
from colours import Colours

pygame.init()

block_char = "#"
area_width = 8
area = ["########",
        "#      #",
        "#      #",
        "#      #",
        "#  #   #",
        "#   #  #",
        "#      #",
        "########"]

area = [list(row) for row in area]

info = pygame.display.Info()
width, height = info.current_w, info.current_h
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Raycasting FPS")

# frame variables
clock = pygame.time.Clock()
fps = 30
frame = -1

# player variables
player_x, player_y = (width // 2) // 2, height // 2
fov = math.pi / 3
half_fov = fov / 2
player_angle = math.pi
player_speed = 5
forward = True

# casting variables
casted_rays = 128
step_angle = fov / (casted_rays - 1)
max_depth = int(math.sqrt((two_d_area_width * two_d_block_width) ** 2 + (two_d_area_width * two_d_block_height) ** 2))
scale = int((width / 2) / casted_rays)

# loop variables
run = True


# function to draw 2d map
def draw_2d_map():
    # drawing the 2d map
    for y in range(len(area)):
        for x in range(len(area[y])):
            pygame.draw.rect(win, block_colour if area[y][x] == block_char else back_colour,
                             pygame.Rect(x * two_d_block_width, y * two_d_block_height, two_d_block_width,
                                         two_d_block_height))


# function to draw 2d map lines
def draw_2d_map_lines():
    # drawing horizontal grid lines over the 2d map
    for y in range(1, len(two_d_area)):
        pygame.draw.line(win, (0, 0, 0), (0, y * two_d_block_height), (width // 2, y * two_d_block_height))

    # drawing vertical grid lines over the 2d map
    for x in range(1, len(two_d_area[0])):
        pygame.draw.line(win, (0, 0, 0), (x * two_d_block_width, 0), (x * two_d_block_width, height))


# function to draw the 2d player
def draw_2d_player():
    # drawing the player
    pygame.draw.circle(win, , (player_x, player_y), 8)

    """# drawing player direction line
    pygame.draw.line(win, (0, 0, 255), (player_x, player_y),
                     (player_x - math.sin(player_angle) * 50, player_y + math.cos(player_angle) * 50), 3)

    # drawing player fov lines
    pygame.draw.line(win, (0, 0, 255), (player_x, player_y),
                     (player_x - math.sin(player_angle + half_fov) * 50,
                      player_y + math.cos(player_angle + half_fov) * 50), 3)
    pygame.draw.line(win, (0, 0, 255), (player_x, player_y),
                     (player_x - math.sin(player_angle - half_fov) * 50,
                      player_y + math.cos(player_angle - half_fov) * 50), 3)"""


# raycasting algorithm
def cast_rays():
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

        start_angle += step_angle


# main loop
while run:
    # in-loop frame settings
    clock.tick(fps)
    frame = (frame + 1) % fps

    # adding the fps to the caption
    pygame.display.set_caption(f"Raycasting - {int(round(clock.get_fps()))} fps")

    # checking if the user has closed the window
    if pygame.event.get(pygame.QUIT):
        run = False
        continue

    player_map_x, player_map_y = int(player_x / two_d_block_width), int(player_y / two_d_block_height)

    block = two_d_area[player_map_y][player_map_x]
    if block == block_char:
        diff_x = -math.sin(player_angle) * player_speed
        diff_y = math.cos(player_angle) * player_speed
        if forward:
            player_x -= diff_x
            player_y -= diff_y
        else:
            player_x += diff_x
            player_y += diff_y

    # getting user input
    keys = pygame.key.get_pressed()

    # using user input
    if keys[pygame.K_a]:
        player_angle -= 0.1

    if keys[pygame.K_d]:
        player_angle += 0.1

    if keys[pygame.K_w]:
        forward = True
        player_x += -math.sin(player_angle) * player_speed
        player_y += math.cos(player_angle) * player_speed

    if keys[pygame.K_s]:
        forward = False
        player_x -= -math.sin(player_angle) * player_speed
        player_y -= math.cos(player_angle) * player_speed

    player_map_x, player_map_y = int(player_x / two_d_block_width), int(player_y / two_d_block_height)

    block = two_d_area[player_map_y][player_map_x]

    if block == block_char:
        diff_x = -math.sin(player_angle) * player_speed
        diff_y = math.cos(player_angle) * player_speed
        if forward:
            player_x -= diff_x
            player_y -= diff_y
        else:
            player_x += diff_x
            player_y += diff_y

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (100, 100, 100), pygame.Rect(width // 2, height // 2, width // 2, height // 2))
    pygame.draw.rect(win, (200, 200, 255), pygame.Rect(width // 2, 0, width // 2, height // 2))

    draw_2d_map()

    cast_rays()

    draw_2d_player()

    pygame.display.update()

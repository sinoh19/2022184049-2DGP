import math

from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

center_x = 400
center_y = 300
radius = 200
angle = 0
motion = 'circle'
running = True

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    if not running:
        break

    radian = math.radians(angle)
    x = center_x + radius * math.cos(radian)
    y = center_y + radius * math.sin(radian)

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    angle = (angle + 1) % 360
    delay(0.01)

close_canvas()

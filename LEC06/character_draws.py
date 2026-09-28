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
square_side = 0
triangle_side = 0
running = True

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    if not running:
        break

    if motion == 'circle':
        radian = math.radians(angle)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)

        if angle == 360:
            motion = 'square'
            x = 600
            y = 300
        else:
            angle += 1

    elif motion == 'square':
        if square_side == 0:
            y += 4
            if y >= 500:
                square_side = 1
        elif square_side == 1:
            x -= 4
            if x <= 200:
                square_side = 2
        elif square_side == 2:
            y -= 4
            if y <= 100:
                square_side = 3
        elif square_side == 3:
            x += 4
            if x >= 600:
                square_side = 4
        elif square_side == 4:
            y += 4
            if y >= 300:
                motion = 'triangle'

    elif motion == 'triangle':
        if triangle_side == 0:
            x -= 4
            y += 4
            if x <= 400:
                triangle_side = 1

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    delay(0.01)

close_canvas()

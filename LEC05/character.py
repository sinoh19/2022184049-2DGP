from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
# 원운동의 중심과 반지름
center_x = 400
center_y = 300
radius = 200
angle = 0

running = True
delay(5)

while running:
    radian = math.radians(angle)
    x = center_x + radius * math.cos(radian)
    y = center_y + radius * math.sin(radian)

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()


    angle = (angle + 1) % 360
    delay(0.01)

running = True


close_canvas()


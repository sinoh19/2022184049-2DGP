import math
from pathlib import Path
from time import perf_counter

import pico2d


WIDTH, HEIGHT = 800, 600
CENTER = (400, 300)
RADIUS = 200
SPEED = 240.0  # Pixels per second, including diagonal movement.
FPS = 60
IMAGE_DIR = Path(__file__).resolve().parent

SQUARE = ((600, 300), (600, 500), (200, 500),
          (200, 100), (600, 100), (600, 300))
TRIANGLE = ((600, 300), (400, 500), (200, 300), (600, 300))


def path_length(points):
    return sum(math.dist(start, end)
               for start, end in zip(points, points[1:]))


CIRCLE_LENGTH = math.tau * RADIUS
SQUARE_LENGTH = path_length(SQUARE)
TRIANGLE_LENGTH = path_length(TRIANGLE)
CYCLE_LENGTH = CIRCLE_LENGTH + SQUARE_LENGTH + TRIANGLE_LENGTH


def polygon_position(points, distance):
    for start, end in zip(points, points[1:]):
        length = math.dist(start, end)
        if distance <= length:
            ratio = distance / length
            return (start[0] + (end[0] - start[0]) * ratio,
                    start[1] + (end[1] - start[1]) * ratio)
        distance -= length
    return points[-1]


def position_at(distance):
    # Carry surplus distance into the next motion, even after a slow frame.
    distance %= CYCLE_LENGTH
    if distance < CIRCLE_LENGTH:
        angle = distance / RADIUS
        return (CENTER[0] + RADIUS * math.cos(angle),
                CENTER[1] + RADIUS * math.sin(angle))

    distance -= CIRCLE_LENGTH
    if distance < SQUARE_LENGTH:
        return polygon_position(SQUARE, distance)

    return polygon_position(TRIANGLE, distance - SQUARE_LENGTH)


def main():
    pico2d.open_canvas(WIDTH, HEIGHT)
    try:
        grass = pico2d.load_image(str(IMAGE_DIR / 'grass.png'))
        character = pico2d.load_image(str(IMAGE_DIR / 'character.png'))
        distance = 0.0
        previous_time = perf_counter()

        while True:
            frame_start = perf_counter()
            if any(event.type == pico2d.SDL_QUIT
                   for event in pico2d.get_events()):
                break

            distance = (distance + SPEED * (frame_start - previous_time)) % CYCLE_LENGTH
            previous_time = frame_start
            x, y = position_at(distance)

            pico2d.clear_canvas()
            grass.draw(WIDTH // 2, 30)
            character.draw(x, y)
            pico2d.update_canvas()

            remaining = 1.0 / FPS - (perf_counter() - frame_start)
            if remaining > 0:
                pico2d.delay(remaining)
    finally:
        pico2d.close_canvas()


if __name__ == '__main__':
    main()

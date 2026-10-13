from pico2d import *
import random

# 마지막 최종 커밋 점검


# Game object class here
# Grass Class 만들기
class Grass:
    pass

# Boy Class 만들기
class Boy:
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()



close_canvas()

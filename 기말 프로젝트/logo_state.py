from pico2d import *
import gfw
import title_state
import time
from gobj import *
def enter():
    global image,elapsed
    image=load_image(RES_DIR +'시작UI.png')
    elapsed=0
def update():
    global elapsed
    elapsed+=gfw.delta_time
    if elapsed>1.0:
        gfw.change(title_state)

def draw():
    image.draw(640,360)

def handle_event(e):
     if e.type == SDL_QUIT:
          gfw.quit()
     elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
          gfw.quit()

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass


if __name__=='__main__':
    gfw.run_main()
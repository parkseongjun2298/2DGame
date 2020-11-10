from pico2d import *
import gfw
import horz_state
from gobj import *

def enter():
    global image
    image=load_image(RES_DIR +'/land0001_tm001_bg1.png')

def update():
    pass

def draw():
    image.draw(640,360)

def handle_event(e):
     if e.type == SDL_QUIT:
          gfw.quit()
     elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
          gfw.quit()
     elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
          gfw.push(horz_state)
def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass


if __name__=='__main__':
    gfw.run_main()
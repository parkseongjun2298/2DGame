from pico2d import *
import gfw
from gobj import *
import title_state

def enter():
    global grass,boy
    grass=Grass()
    boy=Boy()

def update():
    boy.update()

def draw():
    grass.draw()
    boy.draw()

def handle_event(e):
     if e.type == SDL_QUIT:
          gfw.quit()
     elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
          gfw.pop()


def exit():
    pass

if __name__=='__main__':
    gfw.run_main()
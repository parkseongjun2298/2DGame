import gfw
from pico2d import *
from player import Player
from background import  Background
import gobj
import title_state
def enter():
    gfw.world.init(['background', 'player'])
    #넣는 순서 맨뒤부터임
    global  player
    player = Player()
    gfw.world.add(gfw.layer.player,player)
    global background
    background=Background()
    gfw.world.add(gfw.layer.background, background)
def update():
    gfw.world.update()


def draw():
    gfw.world.draw()

    gobj.draw_collision_box()


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()



    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
from pico2d import *
import gfw
import horz_state
from player import Player
from gobj import *


def enter():
    global image
    image = load_image(RES_DIR + '/cookie_run_bg_1.png')
    global player
    player = Player()
    global music_bg
    music_bg = load_music('res/Lobby.ogg')
    music_bg.repeat_play()
def update():
    pass


def draw():
    image.draw(640, 360)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif e.type == SDL_MOUSEBUTTONDOWN:
        mposx = mouse_x(e)
        if mposx <= 550:
            Temp.temp=0
            player.imagenum=0
            gfw.push(horz_state)

        if mposx > 550:
            Temp.temp = 1
            player.imagenum=1
            gfw.push(horz_state)


def exit():
    global image
    del image
    global music_bg
    del music_bg

def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()

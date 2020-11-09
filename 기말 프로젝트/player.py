import random
from pico2d import *
import gfw

from gobj import *


class IdleState:
    @staticmethod
    def get(player):
        if not hasattr(IdleState, 'singleton'):
            IdleState.singleton = IdleState()
            IdleState.singleton.player = player
        return IdleState.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/GingerCookie2-002.png')
    def enter(self):
        self.time = 0
        self.fidx = 0

    def exit(self):
        pass

    def draw(self):
        width = 291
        height = 291
        sx = self.fidx * width

        self.image.clip_draw(sx, 0, width, height, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time

        frame = self.time * 5
        self.fidx = int(frame) % 8

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Player.KEYDOWN_SPACE:
            self.player.set_state(FireState)
            # 슬라이드추가


class FireState:
    @staticmethod
    def get(player):
        if not hasattr(FireState, 'singleton'):
            FireState.singleton = FireState()
            FireState.singleton.player = player
        return FireState.singleton

    def __init__(self):
        self.player = None
        self.image = gfw.image.load(RES_DIR + '/GingerCookie2-003.png')
        self.radius = self.image.h // 2

        self.delta = [0, 1]

    def enter(self):
        self.time = 0
        self.fidx = 0
        self.test = 0

    def exit(self):
        pass

    def draw(self):
        width = 291
        height = 291
        sx = self.fidx * width
        x, y = self.player.pos
        self.image.clip_draw(sx, 0, width, height, x, y)

    def update(self):
        self.time += gfw.delta_time
        self.test += gfw.delta_time / 10


        gravity = 0.005
        self.test -= gravity
        self.delta[1] += self.test
        self.player.delta = point_add(self.player.delta, self.delta)
        move_obj(self.player)
        print(self.player.pos)

        if self.player.pos[1] < 200:
            self.delta[1] = 0
            init_delta(self.player, 0, 0)
            self.test = 0
            #self.time=0
            set_pos(self.player, 100, 200)


        frame = self.time * 7
        if frame < 8:
            self.fidx = int(frame)
        else:
            self.player.set_state(IdleState)


    def handle_event(self, e):
        pass


class Player:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    # constructor

    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = [100, 200]
        self.x, self.y = 100, 200
        self.delta = [0, 0]
        self.fidx = 0
        self.target = None
        self.targets = []
        self.speed = 0
        self.time = 0
        self.state = None
        self.set_state(IdleState)
        self.image = gfw.image.load(RES_DIR + '/GingerCookie2-002.png')
        self.image2 = gfw.image.load(RES_DIR + '/GingerCookie2-003.png')

    def set_state(self, clazz):
        if self.state != None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()

    def draw(self):
        self.state.draw()

    def update(self):
        self.state.update()

    def fire(self):
        self.time = 0
        self.set_state(FireState)

    def get_bb(self):
        hw = self.x // 2
        hh = self.y // 2
        return self.pos[0] - hw, self.pos[1] - hh, self.pos[0] + hw + 25, self.pos[1] + hh - 35

    def handle_event(self, e):
        self.state.handle_event(e)

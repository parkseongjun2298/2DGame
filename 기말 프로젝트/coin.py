import random
from pico2d import *
import gfw
import gobj

COIN_BORDER = 1
COIN_SIZE = 156
BB_RADIUS = COIN_SIZE/2

def get_ITEM_rect(index):
    ix, iy = index % 1, index // 1
    x = ix * (COIN_BORDER + COIN_SIZE) + COIN_BORDER
    y = iy * (COIN_BORDER + COIN_SIZE) + COIN_BORDER
    return x, y, COIN_SIZE, COIN_SIZE


class Coin:
    TYPE_1, TYPE_R = range(2)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('coin.png'))
        index = random.randint(1, 1) if type == Coin.TYPE_R else type
        self.rect = get_ITEM_rect(index)
        self.score=0
    def update(self): pass
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + COIN_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS,
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )


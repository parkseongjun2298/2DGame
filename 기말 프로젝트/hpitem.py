import random
from pico2d import *
import gfw
import gobj

HPITEM_BORDER = 1
HPITEM_SIZE = 136
BB_RADIUS = HPITEM_SIZE/2

def get_ITEM_rect(index):
    ix, iy = index % 1, index // 1
    x = ix * (HPITEM_BORDER + HPITEM_SIZE) + HPITEM_BORDER
    y = iy * (HPITEM_BORDER + HPITEM_SIZE) + HPITEM_BORDER
    return x, y, HPITEM_SIZE, HPITEM_SIZE


class Hpitem:
    TYPE_1, TYPE_R = range(2)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('hpitem.png'))
        index = random.randint(1, 1) if type == Hpitem.TYPE_R else type
        self.rect = get_ITEM_rect(index)
    def update(self): pass
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + HPITEM_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS,
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )


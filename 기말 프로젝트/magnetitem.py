import random
from pico2d import *
import gfw
import gobj

MAGNETITEM_BORDER = 1
MAGNETITEM_SIZE = 87
BB_RADIUS = MAGNETITEM_SIZE/2

def get_ITEM_rect(index):
    ix, iy = index % 1, index // 1
    x = ix * (MAGNETITEM_BORDER + MAGNETITEM_SIZE) + MAGNETITEM_BORDER
    y = iy * (MAGNETITEM_BORDER + MAGNETITEM_SIZE) + MAGNETITEM_BORDER
    return x, y, MAGNETITEM_SIZE, MAGNETITEM_SIZE


class MagnetItem:
    TYPE_1, TYPE_R = range(2)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('magnet.png'))
        index = random.randint(1, 1) if type == MagnetItem.TYPE_R else type
        self.rect = get_ITEM_rect(index)
    def update(self): pass
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + MAGNETITEM_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS,
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )


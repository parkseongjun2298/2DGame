import random
from pico2d import *
import gfw
import gobj

FIREITEM_BORDER = 1
FIREITEM_SIZE = 90
BB_RADIUS = FIREITEM_SIZE/2

def get_ITEM_rect(index):
    ix, iy = index % 1, index // 1
    x = ix * (FIREITEM_BORDER + FIREITEM_SIZE) + FIREITEM_BORDER
    y = iy * (FIREITEM_BORDER + FIREITEM_SIZE) + FIREITEM_BORDER
    return x, y, FIREITEM_SIZE, FIREITEM_SIZE


class FireItem:
    TYPE_1, TYPE_R = range(2)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('fire.png'))
        index = random.randint(1, 1) if type == FireItem.TYPE_R else type
        self.rect = get_ITEM_rect(index)
    def update(self): pass
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + FIREITEM_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS,
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )


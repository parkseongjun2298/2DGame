import random
from pico2d import *
import gfw

from gobj import *


class Background:
    def __init__(self):
        self.x,self.y = 640, 360
        self.time = 0
        self.image = load_image(RES_DIR +'/land0001_tm001_bg1.png')

    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        self.time += gfw.delta_time
        self.x-=self.time/50



if __name__=='__main__':
    gfw.run_main()
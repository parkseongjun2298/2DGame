import random
from pico2d import *
class Grass:
    def __init__(self):
        self.image=load_image('res/grass.png')
        self.x, self.y = 400, 30
    def draw(self):
        self.image.draw(self.x,self.y)

class Boy:
    def __init__(self):
             self.x,self.y=0,90
             self.frame=0
             self.image=load_image('res/run_animation.png')
    def update(self):
                self.frame=(self.frame+1)%8
                self.x+=5
    def draw(self):
                self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


if __name__ == "__main__":
    print("내이름은 "+ __name__ +"이야")


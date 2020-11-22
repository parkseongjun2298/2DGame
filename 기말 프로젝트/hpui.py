from pico2d import *
import gfw
import gobj

from gobj import *

class Hpui:
   def __init__(self):

     self.image = gfw.image.load(gobj.res('HpUi.png'))

   def update(self):
      pass

   def draw(self):
      self.image.clip_draw(0,0,100,100,340,600,75,75)

   def handle_event(self,e):
      pass

   def exit(self):
      global image
      del image



if __name__ == '__main__':
    gfw.run_main()

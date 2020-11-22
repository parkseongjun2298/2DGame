from pico2d import *
import gfw
import gobj

from gobj import *

class Coinui:
   def __init__(self):

     self.image = gfw.image.load(gobj.res('coinui.png'))

   def update(self):
      pass

   def draw(self):
      self.image.clip_draw(0,0,100,100,50,400,50,50)

   def handle_event(self,e):
      pass

   def exit(self):
      global image
      del image



if __name__ == '__main__':
    gfw.run_main()

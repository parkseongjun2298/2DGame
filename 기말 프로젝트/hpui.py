from pico2d import *
import gfw
import horz_state

from gobj import *

class Hpui:
   def __init__(self):
    self.temp=0

   def enter(self):
     global image
     image = load_image(RES_DIR + '/HpUi.png')

   def update(self):
      pass

   def draw(self):
     global image
     image.draw(640, 360)

   def handle_event(self,e):
            pass
   def exit(self):
            global image
            del image



if __name__ == '__main__':
    gfw.run_main()

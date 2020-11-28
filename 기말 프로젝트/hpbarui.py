from pico2d import *
import gfw
import gobj

from gobj import *

class Hpbarui:
   def __init__(self):
     self.sizex=530
     self.sizex2=650
     self.image = gfw.image.load(gobj.res('hpbar.png'))
     self.die=False
   def update(self):
      self.sizex -= 0.25
      self.sizex2-=0.125
      if self.sizex <=0:
         self.die=True



   def draw(self):
      self.image.clip_draw(0,0,530,50,self.sizex2,600,self.sizex,30)

   def handle_event(self,e):
      pass

   def exit(self):
      global image
      del image



if __name__ == '__main__':
    gfw.run_main()

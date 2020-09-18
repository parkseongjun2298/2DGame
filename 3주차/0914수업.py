Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pico2d
Pico2d is prepared.
>>> pico2d.open_canvas()
>>> pico2d.hide_lattice()
>>> 
>>> pico2d.show_lattice()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
>>> p.close_canvas()
>>> from random import uniform as rndf
>>> rndf(0.1,0.5)
0.4557894025914657
>>> from random import*
>>> randrange(10,20)
10
>>> random()
0.8979283144306731
>>> from pico2d import *
>>> load_image('C:\Users\박성준\Desktop\2D겜플')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> import os
>>> os.getcwd()
'C:\\Users\\박성준\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.chdir('C:\Users\박성준\Desktop\2D겜플')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir('C:/Users/박성준/Desktop/2D겜플')
>>> os.getcwd()
'C:\\Users\\박성준\\Desktop\\2D겜플'
>>> os.listdir()
['0903.txt', '0907.txt', '0914.TXT', '0917.TXT', 'animation_sheet.png', 'character.png', 'grass.png', 'LEC01_파이썬기초(1).pdf', 'LEC02_파이썬기초(2).pdf', 'LEC03_파이썬기초(3).pdf', 'LEC04_2D렌더링.pdf', 'LEC05_애니메이션.pdf', 'LEC06_입력처리.pdf', 'LEC07_직선이동.pdf', 'LEC08_곡선이동.pdf', 'LEC09_게임오브젝트.pdf', 'run_animation.png']
>>> load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    load_image('grass.png')
  File "C:\Users\박성준\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> open_canvas()
>>> load_image('grass.png')
<pico2d.pico2d.Image object at 0x000001D16522CEB0>
>>> grass=load_image('grass.png')
>>> case
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    case
NameError: name 'case' is not defined
>>> grass
<pico2d.pico2d.Image object at 0x000001D1651F6400>
>>> grss.draw_now(200,400)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    grss.draw_now(200,400)
NameError: name 'grss' is not defined
>>> grass.draw_now(200,400)
>>> char=load_image('character.png')
>>> char.draw_now(200,500)
>>> 
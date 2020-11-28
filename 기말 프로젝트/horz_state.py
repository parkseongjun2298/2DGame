import random
import gfw
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform

from hpui import Hpui
from hpbarui import Hpbarui
from jellyui import Jellyui
from coinui import Coinui

from jelly import Jelly
from item import Item
from fireitem import FireItem
from coin import Coin
from hpitem import Hpitem

import stage_gen

canvas_width = 1120
canvas_height = 630


SCORE_TEXT_COLOR=(255,255,255)
def enter():
    gfw.world.init(['bg', 'platform', 'enemy', 'jelly','coin','item','hpitem','fireitem', 'player','ui'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,100)]:
        bg = HorzScrollBackground('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    global hpui
    hpui=Hpui()
    gfw.world.add(gfw.layer.ui, hpui)

    global hpbar
    hpbar = Hpbarui()
    gfw.world.add(gfw.layer.ui, hpbar)

    global coinui
    coinui=Coinui()
    gfw.world.add(gfw.layer.ui, coinui)

    global jellyui
    jellyui = Jellyui()
    gfw.world.add(gfw.layer.ui, jellyui)
    global font,score,jellyscore
    stage_gen.load(gobj.res('stage_01.txt'))
    font = gfw.font.load('res/CookieRun Bold.ttf', 35)
    score = 0
    jellyscore=0
paused = False
def update():
    if paused:
        return
    if player.fin==True:
        return
    if hpbar.die==True:
       player.die=True
    global score,jellyscore
    gfw.world.update()

    dx = -300 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.fireitem+1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx*player.FireSpeed) #안에값 커지면 빨라짐


    check_items()
    check_fireitems()
    check_hpitems()
    check_jelly()
    check_obstacles()
    check_coin()
    stage_gen.update(dx)




def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            player.BigCheck=True

            break
def check_fireitems():
    for fireitem in gfw.world.objects_at(gfw.layer.fireitem):
        if gobj.collides_box(player, fireitem):
            gfw.world.remove(fireitem)
            player.FireCheck = True

            break
def check_hpitems():
    for hpitem in gfw.world.objects_at(gfw.layer.hpitem):
        if gobj.collides_box(player, hpitem):
            gfw.world.remove(hpitem)
            hpbar.sizex += 20
            hpbar.sizex2 += 10
            break
def check_jelly():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        if gobj.collides_box(player, jelly):
            gfw.world.remove(jelly)
            global jellyscore
            jellyscore+=33
            break
def check_coin():
    for coin in gfw.world.objects_at(gfw.layer.coin):
        if gobj.collides_box(player, coin):
            gfw.world.remove(coin)
            global score
            score+=10
            break

def check_obstacles():
    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if enemy.hit: continue

        if gobj.collides_box(player, enemy):
            print('Hit', enemy)

            enemy.hit = True
            if player.BigCheck==True:
                hpbar.sizex -=0
                hpbar.sizex2-=0
            elif player.FireCheck==True:
                 hpbar.sizex -=0
                 hpbar.sizex2-=0

            else:
                hpbar.sizex -= 10
                hpbar.sizex2 -=5

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    score_pos = get_canvas_height()//2-225, get_canvas_height()//2+85
    font.draw(*score_pos, '%.0f'%score , SCORE_TEXT_COLOR)
    jellyscore_pos=get_canvas_height()//2+55, get_canvas_height()//2+210
    font.draw(*jellyscore_pos, '%.0f' % jellyscore, SCORE_TEXT_COLOR)


def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif e.key == SDLK_a:
            # player.pos = 150,650
            # for x, y in [(100,400),(400,300),(650,250),(900,200)]:
            for i in range(10):
                x = random.randint(100, 900)
                y = random.randint(200, 400)
                pf = Platform(Platform.T_3x1, x, y)
                gfw.world.add(gfw.layer.platform, pf)
        elif e.key == SDLK_p:
            global paused
            paused = not paused

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()

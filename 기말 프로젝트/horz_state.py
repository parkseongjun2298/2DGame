import random
import gfw
from pico2d import *
import gobj
from player import Player
from player2 import Player2
from player3 import Player3
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
from magnetitem import MagnetItem

import stage_gen
import title_state
canvas_width = 1120
canvas_height = 630


SCORE_TEXT_COLOR=(255,255,255)
SCORE_END_COLOR=(0,0,0)
SCORE_END_COLOR2=(255,0,0)
def enter():
    gfw.world.init(['bg', 'platform', 'enemy', 'jelly','coin','item','hpitem','magnetitem','fireitem', 'player','ui'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,100)]:
        bg = HorzScrollBackground('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)
    global charnum

    global player
    if charnum==0:
        player = Player()
    if charnum==1:
        player = Player2()
    if charnum==2:
        player = Player3()

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

    global music_bg, wav_item,wav_hit,wav_jelly,wav_death,wav_coin,wav_itembig,wav_itembuster,wav_itemmagnet
    music_bg = load_music('res/Land1.ogg')
    wav_itemmagnet=load_wav('res/i_magnet.ogg')
    wav_item = load_wav('res/i_hp.ogg')
    wav_itembig= load_wav('res/i_giant.ogg')
    wav_itembuster= load_wav('res/i_buster.ogg')
    wav_hit= load_wav('res/Collide.ogg')
    wav_jelly= load_wav('res/Jelly.ogg')
    wav_coin= load_wav('res/g_coin.ogg')
    wav_death= load_wav('res/Death.ogg')
    music_bg.repeat_play()

    global game_over_image
    game_over_image = gfw.image.load('res/score.png')
    global hiteffect
    hiteffect = gfw.image.load('res/lowHpScreen.png')





paused = False
def update():

    if paused:
        return
    if player.fin==True:
        music_bg.stop()
        return
    if hpbar.die==True:
       wav_death.play()
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
    check_magnetitems()
    check_jelly()
    check_obstacles()
    check_coin()
    stage_gen.update(dx)


    if player.magnet == True:
        follow_mouse_target()

def follow_mouse_target():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        dx, dy = player.pos[0] - jelly.x, player.pos[1] - jelly.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        elif distance <= 300:
            jelly.x-=0.01*player.pos[0]
            jelly.y += 0.01 * (player.pos[1]-240)
    for coin in gfw.world.objects_at(gfw.layer.coin):
        dx, dy = player.pos[0] - coin.x, player.pos[1] - coin.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        elif distance <= 300:
            coin.x-=0.01*player.pos[0]
            coin.y += 0.01 * (player.pos[1]-240)
    for item in gfw.world.objects_at(gfw.layer.item):
        dx, dy = player.pos[0] - item.x, player.pos[1] - item.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        elif distance <= 300:
            item.x-=0.01*player.pos[0]
            item.y += 0.01 * (player.pos[1]-240)
    for fireitem in gfw.world.objects_at(gfw.layer.fireitem):
        dx, dy = player.pos[0] - fireitem.x, player.pos[1] - fireitem.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        elif distance <= 300:
            fireitem.x-=0.01*player.pos[0]
            fireitem.y += 0.01 * (player.pos[1]-240)
    for hpitem in gfw.world.objects_at(gfw.layer.hpitem):
        dx, dy = player.pos[0] - hpitem.x, player.pos[1] - hpitem.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return
        elif distance <= 300:
            hpitem.x-=0.01*player.pos[0]
            hpitem.y += 0.01 * (player.pos[1]-240)




def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            player.BigCheck=True
            wav_itembig.play()

            break
def check_fireitems():
    for fireitem in gfw.world.objects_at(gfw.layer.fireitem):
        if gobj.collides_box(player, fireitem):
            gfw.world.remove(fireitem)
            player.FireCheck = True
            wav_itembuster.play()
            break
def check_magnetitems():
    for magnetitem in gfw.world.objects_at(gfw.layer.magnetitem):
        if gobj.collides_box(player, magnetitem):
            gfw.world.remove(magnetitem)
            player.magnet=True
            wav_itemmagnet.play()
            break
def check_hpitems():
    for hpitem in gfw.world.objects_at(gfw.layer.hpitem):
        if gobj.collides_box(player, hpitem):
            gfw.world.remove(hpitem)
            hpbar.sizex += 20
            hpbar.sizex2 += 10
            wav_item.play()
            break
def check_jelly():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        if gobj.collides_box(player, jelly):
            gfw.world.remove(jelly)
            global jellyscore
            jellyscore+=33
            wav_jelly.play()
            break
def check_coin():
    for coin in gfw.world.objects_at(gfw.layer.coin):
        if gobj.collides_box(player, coin):
            gfw.world.remove(coin)
            global score
            score+=10
            wav_coin.play()
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
                player.hitcheck=True
                hpbar.sizex -= 10
                hpbar.sizex2 -=5
                wav_hit.play()




def draw():
    gfw.world.draw()
    #gobj.draw_collision_box()
    score_pos = get_canvas_height()//2-225, get_canvas_height()//2+85
    font.draw(*score_pos, '%.0f'%score , SCORE_TEXT_COLOR)
    jellyscore_pos=get_canvas_height()//2+55, get_canvas_height()//2+210
    font.draw(*jellyscore_pos, '%.0f' % jellyscore, SCORE_TEXT_COLOR)
    if player.hitcheck==True:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3-100
        hiteffect.clip_draw(0,0,256,256,*center,1100,600)
        player.hitcheck = False


    if player.fin == True:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        game_over_image.draw(*center)
        score_pos = get_canvas_height() // 2+350 , get_canvas_height() // 2+90
        font.draw(*score_pos, '%.0f' % score, SCORE_END_COLOR)
        jellyscore_pos = get_canvas_height() // 2+350 , get_canvas_height() // 2+60
        font.draw(*jellyscore_pos, '%.0f' % jellyscore, SCORE_END_COLOR)
        finalscore=score+jellyscore
        finalscore_pos= get_canvas_height() // 2 +210 , get_canvas_height() // 2 +135
        font.draw(*finalscore_pos, '%.0f' % finalscore, SCORE_END_COLOR2)

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
    elif e.type == SDL_MOUSEBUTTONDOWN:
        gfw.change(title_state)


    if player.handle_event(e):
        return

def exit():
        global music_bg, wav_item,wav_hit,wav_jelly
        del music_bg
        del wav_item
        del wav_hit
        del wav_jelly



if __name__ == '__main__':
    gfw.run_main()

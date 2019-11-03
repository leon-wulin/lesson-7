# -*- coding: UTF-8 -*-
#writen by leon
#writen time: 2019/10/26
#from machine.standerd_machine import creat_new_deck,shuffled_deck,record_deck
from machine.standerd_machine import *
import time
import os

# import our modules
from display.menu import *
from display.show import *
# Phase 1-----------------------------------------------------------------------
# 打印开始界面
dsp_start()
time.sleep(1)  # 延迟3秒

# Phase 2-----------------------------------------------------------------------
# 打印选择游戏玩法界面
game_type = dsp_choice_game()
deck=[]


if(game_type==1 or game_type==2 or game_type==3 or game_type==4):
    make_deck_by_type(game_type,deck)

else:
    dsp_end()
    exit()

player_a=[]
piayer_b=[]
player_c=[]
player_d=[]
'''

machine.standerd_machine.creat_new_deck(deck)

print(deck)

machine.standerd_machine.record_deck(deck,'deck1.txt')

machine.standerd_machine.shuffled_deck(deck)

machine.standerd_machine.record_deck(deck,'deck2.txt')
'''

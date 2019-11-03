# -*- coding: UTF-8 -*-
#writen by leon
#writen time: 2019/10/26
#from machine.standerd_machine import creat_new_deck,shuffled_deck,record_deck
import machine.standerd_machine

deck=[]

machine.standerd_machine.creat_new_deck(deck)

print(deck)

machine.standerd_machine.record_deck(deck,'deck1.txt')

machine.standerd_machine.shuffled_deck(deck)

machine.standerd_machine.record_deck(deck,'deck2.txt')

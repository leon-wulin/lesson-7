# -*- coding: UTF-8 -*-

# author by:leon
#created: 2019/10/26
import random
import codecs
import copy
import os
cardJokers = ('♞', '♘')
cardMarks = ('♠', '♥', '♦', '♣')

cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')


def creat_new_deck(new_deck):
    "Desc:make a new standard 54 cards, in orders"

    #new_deck = []

    # add jokers first
    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 card
    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)

    return


def shuffled_deck(deck):
    "Desc:shuffle the deck"
    random.shuffle(deck)
    return


def record_deck(deck, filename):
    "Desc:Write a deck into a specified deck"
    out_path = os.getcwd() + '\\out_put_decks\\' + filename
    f = codecs. open(out_path, 'w', 'utf-8')

    for card in deck:
        f.write(card)
        f.write('\n')
    f.close()
    return
    

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


def create_deck_54(new_deck):
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

def create_deck_52(new_deck):
    "Desc:make a new standard 54 cards, in orders"

    #new_deck = []

    # add jokers first
#    for c in cardJokers:
    #    new_deck.append(c)

    # add 4x13 card
    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)

    return

def shuffled_deck(deck_to_be_shuffled):
    "Desc:shuffle the deck"
    print('\n--debug: I shuffled a deck')
    random.shuffle(deck_to_be_shuffled)
    return

def record_deck(deck_to_be_record, filename):
    "Desc:Write a deck into a specified deck"
    out_path = os.getcwd() + '\\out_put_decks\\' + filename
    f = codecs. open(out_path, 'w', 'utf-8')

    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close()
    return

def make_deck_by_type(player_type,out_deck):
    '按照要求制作各种扑克牌'
    if player_type==1:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck,"争上游-刚洗好的牌.txt")
    if player_type==2:
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck,"桥牌-刚洗好的牌.txt")
    if player_type==3:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck,"三人斗地主-刚洗好的牌.txt")
    if player_type==4:
        deck_a=[]
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        deck_b=[]
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        shuffled_deck(out_deck)
        record_deck(out_deck,'四人斗地主-刚洗好的牌.txt')
        return

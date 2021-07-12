from player import *
from deck import *
from typing import List
from cards_weight import *
from game import *
from card_collection import *
from notifications import * 


def output():
    for player in players:
        print("%s's -- %d,  cards " % (player.name, CardWeight.get_weight_cards(player.cards)), player.cards)
    print('After dealing: ', deck)


artyom = Player('Artyom')

igor = Player('Igor')

players = [artyom, igor]

cards = []
       
for suit in Card.SUITS:
    for value in Card.VALUES:
        cards.append(Card(value, suit))

deck = Deck(cards)

deck.shuffle()
print('Before dealing: ', deck)
    

g = Game(players, deck)
for player in players:
    g.attach('start', player)
    g.attach('lose', player)
    g.attach('win', player)

g.run()

output()

for player in players:
    take_card = input("%s's Хотите взять еще одну карту? (y/n) " % player.name)

    while True:
        if take_card == 'n':
            g.reject(player)
            break
        
        overflow = g.take_card(player)
        output()
        
        if overflow:
            #TODO: Перебор
            break

        take_card = input("%s's Хотите взять еще одну карту? (y/n) " % player.name)


output()

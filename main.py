from player import *
from deck import *
from typing import List
from cards_weight import *
from game import *
from card_collection import *


artyom = Player('Artyom', [])
igor = Player('Igor', [])

players = [artyom, igor]

cards = []
       
for suit in Card.SUITS:
    for value in Card.VALUES:
        cards.append(Card(value, suit))

deck = Deck(cards)

deck.shuffle()
print('Before dealing: ', deck)

g = Game(players, deck)
g.run()

for player in players:
    print("%s's -- %d,  cards " % (player.name, CardWeight.get_weight_cards(player.cards)), player.cards)
    print('After dealing: ', deck)

for player in players:
    take_card = input("%s's Хотите взять еще одну карту? (y/n) " % player.name)
    if take_card == 'y':
        g.take_cards(player)
     
for player in players:
    print("%s's -- %d,  cards " % (player.name, CardWeight.get_weight_cards(player.cards)), player.cards)
    print('After dealing: ', deck)

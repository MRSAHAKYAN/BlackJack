from player import *
from deck import *
from typing import List
from cards_weight import *


class Game:
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
    
    def run(self):
        #TODO: Раздача по две карты всем игрокам
        for player in self.players:
            self.deck.move_last_cards(player)

        
    def take_cards(self):
        for player in self.players:
            take_card = input("%s's Хотите взять еще одну карту? (y/n) " % player.name)
            if take_card == 'y':
                self.deck.take_card(player)
                weight = CardWeight.get_weight_cards(player.cards)

                print('%s\'s --  %d,    cards: ' % (player.name, weight), player.cards)
                if weight > 21:
                    print('%s is loser' % player.name)
                    
        
        #   if take_card == 'n':
        #        break



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
# Game([artyom, igor], deck).run()

g = Game(players, deck)
g.run()
for player in players:
    print("%s's -- %d,  cards " % (player.name, CardWeight.get_weight_cards(player.cards)), player.cards)
print('After dealing: ', deck)

g.take_cards()
for player in players:
    print("%s's -- %d,  cards " % (player.name, CardWeight.get_weight_cards(player.cards)), player.cards)
print('After dealing: ', deck)


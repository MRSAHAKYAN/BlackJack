from card import *
import random
from player import *


class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def shuffle(self):
       random.shuffle(self.cards)    
       

    def move_last_cards(self, player: Player):
        player.cards += self.cards[-2:]
        del self.cards[-2:]

    def take_a_card(self, player: Player):
        player.cards += self.cards[-1:]
        del self.cards[-1:]

   
    def __str__(self):
        return str(self.cards)

        
        
        
# cards = []
       
# for suit in Card.SUITS:
#     for value in Card.VALUES:
#         cards.append(Card(value, suit))

# deck = Deck(cards)
# # deck.shuffle()
# print(deck)
# print(deck.move_last_cards)



# # get_spravka => return


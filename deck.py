from card import *
import random
from player import *
from card_collection import *


class Deck(CardCollection):
    def __init__(self, cards):
        super().__init__(cards)
        
    def shuffle(self):
       random.shuffle(self.cards)    
       

    # def move_last_cards(self, player: Player):
    #     player.cards += self.cards[-2:]
    #     del self.cards[-2:]

    def take_card(self, player: Player):
        player.cards += self.cards[-1:]
        del self.cards[-1:]

    def flip_deck(self):
        for i in range(len(self.cards) // 2):
            self.cards[i], self.cards[-1-i] = self.cards[-1-i], self.cards[i]

    #    self.cards = self.cards[::-1]


    def __str__(self):
        return str(self.cards)

        
    
        
# cards = []
       
# for suit in Card.SUITS:
#     for value in Card.VALUES:
#         cards.append(Card(value, suit))

# deck = Deck(cards)
# deck.flip_deck()   
# print(deck)
# deck.flip_deck()
# # deck.shuffle()

# print(deck.move_last_cards)



# # get_spravka => return


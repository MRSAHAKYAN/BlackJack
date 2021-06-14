from card import *
import random
from player import *
from card_collection import *


class Deck(CardCollection):
    def __init__(self, cards):
        super().__init__(cards)
        
    def shuffle(self):
       random.shuffle(self.cards)    

    def take_card(self, player: Player):
        player.cards += self.cards[-1:]
        del self.cards[-1:]

    def flip_deck(self):
        for i in range(len(self.cards) // 2):
            self.cards[i], self.cards[-1-i] = self.cards[-1-i], self.cards[i]
            
    def __str__(self):
        return str(self.cards)


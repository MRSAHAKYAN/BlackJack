from card import Card
import random
from player import Player
from card_collection import CardCollection


class Deck(CardCollection):
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        super().__init__(cards)
        
    def shuffle(self):
       random.shuffle(self.cards)

    def flip_deck(self):
        for i in range(len(self.cards) // 2):
            self.cards[i], self.cards[-1-i] = self.cards[-1-i], self.cards[i]
            
    def __str__(self):
        return str(self.cards)


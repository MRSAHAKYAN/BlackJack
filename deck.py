from card import *
import random


class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def shuffle(self):
       random.shuffle(self.cards)    

    def get_last_card(self):
        return self.cards.pop()
   
    def __str__(self):
        return str(self.cards)

# last_card = deck.get_last_card()
# last_card = deck.get_last_card()
# last_card = deck.get_last_card()
# last_card = deck.get_last_card()
# last_card = deck.get_last_card()
# last_card = deck.get_last_card()

# for i in range(13):
#     last_card = deck.get_last_card()
#     print(last_card)

# print(deck)
# print(last_card)




# deck.shuffle()

# print(deck)

# for cards in card:
    
# for ....,
# for...
#     добавление карты в cards
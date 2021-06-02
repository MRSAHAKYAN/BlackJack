from card import *
import random


class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def shuffle(self):
       random.shuffle(self.cards)    

    def get_last_cards(self):
       return self.cards[-4:]
    #    return (self.cards[-4:])

    # def delete_last_cards(self):
    #     return  del self.cards[-4:0]
   
    def __str__(self):
        return str(self.cards)

        
        
        
cards = []
       
for suit in Card.SUITS:
    for value in Card.VALUES:
        cards.append(Card(value, suit))

deck = Deck(cards)
deck.shuffle()
print(deck.get_last_cards())


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
from player import *
from deck import *
from typing import List

class Game:
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
    
    def run(self):
        
        #TODO: Тасовка карт
        self.deck.shuffle()
        
        #TODO: Раздача по две карты всем игрокам
        players_card = self.deck.get_last_cards()
        # self.players = player
        
        
        # return  players_card



artyom = Player('Artyom', [])
igor = Player('Igor', [])

cards = []
       
for suit in Card.SUITS:
    for value in Card.VALUES:
        cards.append(Card(value, suit))

deck = Deck(cards)

# Game([artyom, igor], deck).run()
Game([igor, artyom], deck).run()

# print(artyom.cards, igor.cards)
# def calculate_force(m, a):
#     return  m * a

# F = calculate_force(5, 3)

# print('F = %d' % (m * a))

# def get_distance(x1, y1, x2, y2):
#     return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



# def print_100():
#     for i in range(1, 101):
#         print(i)

# print_100()

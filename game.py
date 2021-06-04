from player import *
from deck import *
from typing import List

class Game:
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
    
    def run(self):
        
        #TODO: Раздача по две карты всем игрокам
        for player in self.players:
            self.deck.move_last_cards(player)

        # self.players = player
        
        
        # return  players_card



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
    print("%s's cards " % player.name, player.cards)
print('After dealing: ', deck)

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

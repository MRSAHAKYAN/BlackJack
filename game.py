from player import *
from deck import *
from typing import List
from cards_weight import *
from card_collection import *


class Game:
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
    
    def run(self):
        #TODO: Раздача по две карты всем игрокам
        for player in self.players:
            self.deck.move_last_cards(player, 2)
 
    def take_cards(self,player):
        self.deck.take_card(player)
        weight = CardWeight.get_weight_cards(player.cards) 
        if weight > 21:
            print('%s is loser' % player.name)

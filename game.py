from player import *
from deck import *
from typing import List
from cards_weight import *
from card_collection import *
from notifications import *


class Game(Publisher):
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
        self.turn = 0

        self.rejects= {}
    
    def _next(self):
        self.turn += 1

    def run(self):
        #TODO: Раздача по две карты всем игрокам
        for player in self.players:
            self.deck.move_last_cards(player, 2)

        self.notify('start')
        
    def your_turn(func):
        def wrapper(self, player):
           if player == self.players[self.turn]:
            #    return func(self, player) => take_card(self, player) => False
                return func(self, player)
        return wrapper
       
    @your_turn  
    def take_card(self, player: Player) -> bool:
        self.deck.move_last_cards(player, 1)
        weight = CardWeight.get_weight_cards(player.cards)
        if weight > 21:
            self.notify('lose', player.name)
            self._next()
            
        return weight > 21
    
    @your_turn
    def reject(self, player: Player):      
        self.rejects[player.name] = 'reject'
        self._next()
        if self.is_finish():
           self.notify('win', self.verdict())
                
    def is_finish(self) -> bool:
        return self.turn == len(self.players) 

    def verdict(self):
        #TODO:
        # 1. Отобрать игроков, у кого не больше 21 очков
        # 2. Выбрать игрока с максимальным количеством очков (из оставшихся)

        pp = list(filter(lambda p: CardWeight.get_weight_cards(p.cards) <= 21, self.players))
        if len(set(pp)) > 1:
            return max(pp, key=lambda p: CardWeight.get_weight_cards(p.cards))
        else:
            return None
from player import Player
from deck import Deck
from typing import List
from cards_weight import CardWeight
from card_collection import CardCollection
from notifications import Publisher


class Game(Publisher):
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
        self.turn = 0
        
    def _next(self):
        self.turn += 1
        if self.is_finish():
            self.notify('win', self.verdict())

    def run(self):
        for player in self.players:
            self.deck.move_last_cards(player, 2)
        self.notify('start')
        
    def your_turn(func):
        def wrapper(self, player):
           if player == self.players[self.turn]:
                return func(self, player)
        return wrapper
       
    @your_turn  
    def take_card(self, player: Player) -> bool:
        ''' Gives one card from the deck to the player '''
        self.deck.move_last_cards(player, 1)
        weight = CardWeight.get_weight_cards(player.cards)
        if weight > 21:
            self._next()
        return weight > 21
    
    @your_turn
    def reject(self, player: Player):    
        self._next()
                
    def is_finish(self) -> bool:
        return self.turn == len(self.players) 

    def verdict(self) -> Player:
        # 1. Выбрать игроков с максимальным количеством очков до 21 включительно => [...]
        # 2. Если у игроков одинаковые очки вернуть ничью
        pp = list(filter(lambda p: CardWeight.get_weight_cards(p.cards) <= 21, self.players))
        scores = set(map(lambda p: CardWeight.get_weight_cards(p.cards), pp))
        if len(scores) > 1 or \
            (len(scores) == 1 and len(pp) == 1):
            return max(pp, key=lambda p: CardWeight.get_weight_cards(p.cards))
        return None


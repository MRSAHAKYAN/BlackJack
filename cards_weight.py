from typing import List
from card import *

class CardWeight:
    WEIGHTS = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
    }

    @staticmethod
    def _get_weight(card: Card) -> int:
        # '2' ... '10' => int('2') => 2
        # J => WEIGHTS => 10
        
        if card.value.isdigit():
            return int(card.value)
        else:
            return CardWeight.WEIGHTS[card.value]
        
    #
    @staticmethod
    def get_weight_cards(cards: List[Card]) -> int:
        total = 0
        for card in cards:
           total += CardWeight._get_weight(card)
    
        return total
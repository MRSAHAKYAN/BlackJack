from typing import List
from card import *

class CardWeight:
    WEIGHTS = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
    }
    
    # def __init__(self, cards: List[Card]):
    #     self.cards = cards

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
        # self.cards = [Card('2', 'H'), Card('7', 'S')]
        total = 0
        for card in cards:
           total += CardWeight._get_weight(card)
    
        return total

# weight = CardWeight([Card('A', 'C'), Card('2', 'S')]).get_weight_cards()
# print(weight)

# cards = [Card('A', 'C'), Card('2', 'S')]
# cw1 = CardWeight(cards)
# cw1.get_weight_cards() => 13

# cw2 = CardWeight(cards)
# cw1.get_weight_cards() => 13

# print(CardWeight.get_weight_cards(cards))

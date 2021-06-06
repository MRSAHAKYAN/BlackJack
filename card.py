        # D - Diamonds (Бубни)
        #  H - Hearts (Червы)
        # C - Clubs (трефы)
        #S - Spades (пики)

class Card:
    ICONS = {
        'H': '♥',
        'C': '♣',
        'S': '♠',
        'D': '♦',
    }
    SUITS = ('H', 'C', 'S', 'D')
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    
    def __init__(self, value, suit):
       self.value = value
       self.suit = suit
    def __str__(self):
        return self.value + Card.ICONS[self.suit]

    def __repr__(self):
        return self.__str__()

# for suit in Card.SUITS:
#     for value in Card.VALUES:
#         print(Card(value, suit))


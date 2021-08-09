class CardCollection:
    def __init__(self, cards):
        self.cards = cards

    def move_last_cards(self, distination, count):
        distination.cards += self.cards[-count:]
        del self.cards[-count:]
from card_collection import *

class Player(CardCollection):
    def __init__(self, name, cards):
        super().__init__(cards)
        self.name = name

    def get_name(self):
        return self.name

    
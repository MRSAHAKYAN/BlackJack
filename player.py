from card_collection import *
from notifications import Observer
from cards_weight import *


class Player(CardCollection, Observer):
    def __init__(self, name, cards=None):
        if cards is None:
            cards = []
            
        super().__init__(cards)
        self.name = name
  
    def get_name(self):
        return self.name

    def update(self, subject: str, data: any):
        if subject == 'start':
            print("%s ready to play" % self.name)
        elif subject == 'lose':
            if self.name == data:
                print('%s: You are a loser' % self.name)
            else:
                print('%s: %s lost' % (self.name, data))

        elif subject == 'win':
            if not data:
                print('%s: Tie' % self.name)
            elif self.name == data.name:
                print('%s: You are a winner' % self.name)
            else:
                print('%s: %s won' % (self.name, data.name))


import unittest
from player import Player
from card import Card
from deck import Deck
from game import Game

    
class TestGame(unittest.TestCase):
    def test_take_card(self):
        cases = [
            {
                'deck': Deck([
                    Card('4', 'H'),
                    Card('5', 'C'), 
                    Card('6', 'S'), 
                    Card('7', 'D'),
                    Card('8', 'H'),
                ]),
                'players': [
                    {
                        'player': Player('Igor', [Card('2', 'H'), Card('3', 'C')]),
                        'want_cards': [Card('2', 'H'), Card('3', 'C'), Card('8', 'H')],
                    },
                    {
                        'player': Player('Artyom', [Card('2', 'S'), Card('3', 'D')]),
                        'want_cards': [Card('2', 'S'), Card('3', 'D')],
                    },
                ],
                'taking_player_index': 0,
                'want_deck_cards': [   
                    Card('4', 'H'),
                    Card('5', 'C'), 
                    Card('6', 'S'),
                    Card('7', 'D'), 
                ],
            },
        ]
        
        for case in cases:
            players = [p.get('player') for p in case['players']]
            
            g = Game(deck=case['deck'], players=players)
            taking_player = players[case.get('taking_player_index')]
            g.take_card(taking_player)
            
            for player in case['players']:
                self.assertEqual(
                    { hash(frozenset(card.__dict__.items())) for card in player['want_cards'] }, 
                    { hash(frozenset(card.__dict__.items())) for card in player['player'].cards },
                )

            self.assertEqual(
                [card.__dict__ for card in case.get('want_deck_cards')], 
                [card.__dict__ for card in case.get('deck').cards],
            )


    def test_verdict(self):
        situations = [
            {
                'players': [
                    Player('Igor', [Card('10', 'C'), Card('A', 'H')]),
                    Player('Artyom', [Card('10', 'H'), Card('A', 'C')]),
                ], 
                'expected': None,
            },
            {
                'players': [
                    Player('Igor', [Card('10', 'C'), Card('9', 'H')]),
                    Player('Artyom', [Card('J', 'S'), Card('5', 'C')]),
                ], 
                'expected': 'Igor',
            },
            {
                'players': [
                    Player('Igor', [Card('10', 'C'), Card('9', 'H'), Card('A', 'D')]),
                    Player('Artyom', [Card('J', 'S'), Card('5', 'C')]),
                ], 
                'expected': 'Artyom',
            },
            {
                'players': [
                    Player('Igor', [Card('10', 'C'), Card('9', 'H'), Card('A', 'D')]),
                    Player('Artyom', [Card('J', 'S'), Card('5', 'C'), Card('A', 'S')]),
                ], 
                'expected': None, 
            },
        ]

        for situation in situations:
            g = Game(deck=Deck(), players=situation['players']) 
            
            winner = g.verdict()
            if winner is not None:
                self.assertEqual(situation['expected'], winner.name)
            else:
                self.assertIsNone(situation['expected'])
            

if __name__ == "__main__":
    unittest.main()
            
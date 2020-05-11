import unittest

# creature removal (unsubscription) ignored in this exercise solution
from Section13_ChainOfResponsability.Practice.Game import Game
from Section13_ChainOfResponsability.Practice.Goblin import Goblin
from Section13_ChainOfResponsability.Practice.GoblinKing import GoblinKing


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)
        game.creatures.append(goblin2)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)
        game.creatures.append(goblin3)

        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)

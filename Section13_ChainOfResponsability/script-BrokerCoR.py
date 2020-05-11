# 1) event broker
# 2) command-query separation (cqs)
# 3) observer

from Section13_ChainOfResponsability.BrokerCoR.Creature import Creature
from Section13_ChainOfResponsability.BrokerCoR.DoubleAttackModifier import DoubleAttackModifier
from Section13_ChainOfResponsability.BrokerCoR.Game import Game
from Section13_ChainOfResponsability.BrokerCoR.IncreaseDefenseModifier import IncreaseDefenseModifier

if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
        with IncreaseDefenseModifier(game, goblin):
            print(goblin)

    print(goblin)

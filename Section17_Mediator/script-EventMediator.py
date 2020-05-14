from Section17_Mediator.EventMediator.Coach import Coach
from Section17_Mediator.EventMediator.Game import Game
from Section17_Mediator.EventMediator.Player import Player

if __name__ == '__main__':
    game = Game()
    player = Player('Sam', game)
    coach = Coach(game)
    player.score()  # Coach says: well done, Sam!
    player.score()  # Coach says: well done, Sam!
    player.score()  # ignored by coach

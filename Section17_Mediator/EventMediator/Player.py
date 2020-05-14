from Section17_Mediator.EventMediator.GoalScoredInfo import GoalScoredInfo


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)

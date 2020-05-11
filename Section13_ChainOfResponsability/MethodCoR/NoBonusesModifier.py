from Section13_ChainOfResponsability.MethodCoR.CreatureModifier import CreatureModifier


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print('No bonuses for you!')

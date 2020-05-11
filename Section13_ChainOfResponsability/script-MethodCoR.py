from Section13_ChainOfResponsability.MethodCoR.Creature import Creature
from Section13_ChainOfResponsability.MethodCoR.CreatureModifier import CreatureModifier
from Section13_ChainOfResponsability.MethodCoR.DoubleAttackModifier import DoubleAttackModifier
from Section13_ChainOfResponsability.MethodCoR.IncreaseDefenseModifier import IncreaseDefenseModifier
from Section13_ChainOfResponsability.MethodCoR.NoBonusesModifier import NoBonusesModifier

if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)
    root = CreatureModifier(goblin)
    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    # no effect
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.handle()  # apply modifiers
    print(goblin)

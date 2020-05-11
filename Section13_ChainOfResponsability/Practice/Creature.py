from abc import ABC


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    def query(self, source, query): pass

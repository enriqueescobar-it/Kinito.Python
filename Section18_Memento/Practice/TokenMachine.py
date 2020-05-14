from copy import deepcopy

from Section18_Memento.Practice.Memento import Memento
from Section18_Memento.Practice.Token import Token


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        self.tokens = [Token(x.value) for x in memento]

from enum import Enum


class Token:
    class TypeEnum(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'

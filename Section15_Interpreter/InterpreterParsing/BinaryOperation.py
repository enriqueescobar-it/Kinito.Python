from enum import Enum


class BinaryOperation:
    class TypeEnum(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.TypeEnum.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.TypeEnum.SUBTRACTION:
            return self.left.value - self.right.value

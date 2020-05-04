from Section01_SOLID.Color import Color
from Section01_SOLID.Specification import Specification


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

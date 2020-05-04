from Section01_SOLID.Size import Size
from Section01_SOLID.Specification import Specification


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

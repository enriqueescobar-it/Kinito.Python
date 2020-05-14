from abc import ABC


class AbstractDiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass

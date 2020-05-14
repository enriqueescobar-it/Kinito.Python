from Section21_Strategy.Practice.AbstractDiscriminantStrategy import AbstractDiscriminantStrategy


class OrdinaryAbstractDiscriminantStrategy(AbstractDiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b * b - 4 * a * c

from Section21_Strategy.Practice.AbstractDiscriminantStrategy import AbstractDiscriminantStrategy


class RealAbstractDiscriminantStrategy(AbstractDiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = b * b - 4 * a * c
        return result if result >= 0 else float('nan')

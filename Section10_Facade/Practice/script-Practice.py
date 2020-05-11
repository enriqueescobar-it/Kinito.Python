from unittest import TestCase

from Section10_Facade.Practice.MagicSquareGenerator import MagicSquareGenerator
from Section10_Facade.Practice.Verifier import Verifier


class Evaluate(TestCase):
    def test_exercise(self):
        gen = MagicSquareGenerator()
        square = gen.generate(3)

        print(square)

        v = Verifier()
        self.assertTrue(v.verify(square),
                        'Verification failed. '
                        'This is not a valid magic square.')

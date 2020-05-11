import unittest

from Section11_Flyweight.Practice.Sentence import Sentence


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')

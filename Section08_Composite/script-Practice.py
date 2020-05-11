from unittest import TestCase

from Section08_Composite.Practice.ManyValues import ManyValues
from Section08_Composite.Practice.SingleValue import SingleValue


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

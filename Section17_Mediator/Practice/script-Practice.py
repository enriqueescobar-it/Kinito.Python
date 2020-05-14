import unittest

from Section17_Mediator.Practice.Mediator import Mediator
from Section17_Mediator.Practice.Participant import Participant


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)
        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)
        p1.say(2)
        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)
        p2.say(4)
        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)

from unittest.case import TestCase

from Section06_Adapter.Practice.Square import Square
from Section06_Adapter.SquareToRectangleAdapter import SquareToRectangleAdapter


class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, self.calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, self.calculate_area(adapter))

    def calculate_area(self, squareLike: SquareToRectangleAdapter):
        return squareLike.width * squareLike.height

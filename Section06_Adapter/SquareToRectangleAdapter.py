from Section06_Adapter.Practice.Square import Square


class SquareToRectangleAdapter:
    def __init__(self, square: Square):
        self.square: Square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

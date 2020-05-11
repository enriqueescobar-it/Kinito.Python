from Section09_Decorator.RegularDecorator.Shape import Shape


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'

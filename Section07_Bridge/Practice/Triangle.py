from Section07_Bridge.Practice.Shape import Shape


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')

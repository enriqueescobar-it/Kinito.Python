from Section04_Prototype.Practice.Point import Point


class Line:
    def __init__(self, start: Point = Point(), end: Point = Point()):
        self.start: Point = start
        self.end: Point = end

    def deep_copy(self):
        new_start: Point = Point(self.start.x, self.start.y)
        new_end: Point = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)

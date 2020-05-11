from Section06_Adapter.AdapterWithCache.Line import Line
from Section06_Adapter.AdapterWithCache.LineToPointAdapter import LineToPointAdapter
from Section06_Adapter.AdapterWithCache.Point import Point
from Section06_Adapter.AdapterWithCache.Rectangle import Rectangle


def draw_point(p):
    print('.', end='')


# ^^ you are given this
# vv you are working with this

def draw(rcs):
    print('Drawing some rectangles...')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print('\n')


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rs)
    draw(rs)

    # can define your own hashes or use the defaults
    print(hash(Line(Point(1, 1), Point(10, 10))))

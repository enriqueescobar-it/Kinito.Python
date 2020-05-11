from Section06_Adapter.AdapterNoCache.LineToPointAdapter import LineToPointAdapter
from Section06_Adapter.AdapterNoCache.Rectangle import Rectangle


def draw_point(p):
    print('.', end='')


# ^^ you are given this
# vv you are working with this
def draw(rcs: []):
    print("\n\n--- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)

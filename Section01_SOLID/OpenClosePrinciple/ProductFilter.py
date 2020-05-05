from Section01_SOLID.OpenClosePrinciple.Color import Color
from Section01_SOLID.OpenClosePrinciple.Size import Size


class ProductFilter:
    def filter_by_color(self, products: [], color: Color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products: [], size: Size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products: [], size: Size, color: Color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods

    # OCP = open for extension, closed for modification

from Section01_SOLID.Filter import Filter
from Section01_SOLID.Specification import Specification


class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item

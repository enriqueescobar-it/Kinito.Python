from Section01_SOLID.OpenClosePrinciple.Filter import Filter


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

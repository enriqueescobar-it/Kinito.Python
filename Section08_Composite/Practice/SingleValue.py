from Section08_Composite.Practice.ValueContainer import ValueContainer


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

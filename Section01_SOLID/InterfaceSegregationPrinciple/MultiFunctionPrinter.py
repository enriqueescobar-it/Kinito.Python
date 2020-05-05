from Section01_SOLID.InterfaceSegregationPrinciple.Machine import Machine


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

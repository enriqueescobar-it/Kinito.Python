from Section01_SOLID.InterfaceSegregationPrinciple.Printer import Printer


class MyPrinter(Printer):
    def print(self, document):
        print(document)

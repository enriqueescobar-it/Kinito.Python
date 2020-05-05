from Section01_SOLID.InterfaceSegregationPrinciple.Printer import Printer
from Section01_SOLID.InterfaceSegregationPrinciple.Scanner import Scanner


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful

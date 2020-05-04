from Section01_SOLID.Printer import Printer
from Section01_SOLID.Scanner import Scanner


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful

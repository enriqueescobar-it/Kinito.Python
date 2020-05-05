from abc import abstractmethod

from Section01_SOLID.InterfaceSegregationPrinciple.Printer import Printer
from Section01_SOLID.InterfaceSegregationPrinciple.Scanner import Scanner


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

from abc import abstractmethod


class Scanner:
    @abstractmethod
    def scan(self, document): pass

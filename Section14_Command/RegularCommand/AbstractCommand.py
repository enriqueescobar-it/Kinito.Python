from abc import ABC


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

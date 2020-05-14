from abc import ABC


class AbstractCommand(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

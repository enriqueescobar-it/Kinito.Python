from abc import ABC


class AbstractCommand(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

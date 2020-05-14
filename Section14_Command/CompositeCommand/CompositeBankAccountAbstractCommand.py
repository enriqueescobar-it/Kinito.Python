from Section14_Command.CompositeCommand.AbstractCommand import AbstractCommand


class CompositeBankAccountAbstractCommand(AbstractCommand, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()

from Section14_Command.CompositeCommand.BankAccountAbstractCommand import BankAccountAbstractCommand
from Section14_Command.CompositeCommand.CompositeBankAccountAbstractCommand import CompositeBankAccountAbstractCommand


class MoneyTransferCommand(CompositeBankAccountAbstractCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountAbstractCommand(from_acct,
                                       BankAccountAbstractCommand.Action.WITHDRAW,
                                       amount),
            BankAccountAbstractCommand(to_acct,
                                       BankAccountAbstractCommand.Action.DEPOSIT,
                                       amount)])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok

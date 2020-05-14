from enum import Enum

from Section14_Command.RegularCommand.AbstractCommand import AbstractCommand


class BankAccountAbstractCommand(AbstractCommand):
    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    class ActionEnum(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action == self.ActionEnum.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.ActionEnum.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.ActionEnum.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.ActionEnum.WITHDRAW:
            self.account.deposit(self.amount)

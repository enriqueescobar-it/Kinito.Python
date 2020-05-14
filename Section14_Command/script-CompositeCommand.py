# Composite Command a.k.a. Macro
# also: Composite design pattern ;)
import unittest

from Section14_Command.CompositeCommand.BankAccount import BankAccount
from Section14_Command.CompositeCommand.BankAccountAbstractCommand import BankAccountAbstractCommand
# try using this before using MoneyTransferCommand!
from Section14_Command.CompositeCommand.CompositeBankAccountAbstractCommand import CompositeBankAccountAbstractCommand
from Section14_Command.CompositeCommand.MoneyTransferCommand import MoneyTransferCommand


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountAbstractCommand(ba, BankAccountAbstractCommand.Action.DEPOSIT, 1000)
        deposit2 = BankAccountAbstractCommand(ba, BankAccountAbstractCommand.Action.DEPOSIT, 1000)
        composite = CompositeBankAccountAbstractCommand([deposit1, deposit2])
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # composite isn't so good because of failure
        amount = 1000  # try 1000: no transactions should happen
        wc = BankAccountAbstractCommand(ba1, BankAccountAbstractCommand.Action.WITHDRAW, amount)
        dc = BankAccountAbstractCommand(ba2, BankAccountAbstractCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountAbstractCommand([wc, dc])

        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)  # end up in incorrect state
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)

    def test_better_tranfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)
        print(transfer.success)

import unittest

from Section14_Command.Practice.Account import Account
from Section14_Command.Practice.AbstractCommand import AbstractCommand


class Evaluate(unittest.TestCase):
    def test(self):
        a = Account()

        cmd = AbstractCommand(AbstractCommand.Action.DEPOSIT, 100)
        a.process(cmd)

        self.assertEqual(100, a.balance)
        self.assertTrue(cmd.success)

        cmd = AbstractCommand(AbstractCommand.Action.WITHDRAW, 50)
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertTrue(cmd.success)

        cmd.amount = 150
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertFalse(cmd.success)

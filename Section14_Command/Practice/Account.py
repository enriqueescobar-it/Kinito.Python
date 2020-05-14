from Section14_Command.Practice.AbstractCommand import AbstractCommand


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == AbstractCommand.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == AbstractCommand.Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount

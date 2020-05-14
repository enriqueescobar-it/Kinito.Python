from Section14_Command.RegularCommand.BankAccount import BankAccount
# optional
from Section14_Command.RegularCommand.BankAccountCommand import BankAccountAbstractCommand

if __name__ == '__main__':
    ba = BankAccount()
    cmd = BankAccountAbstractCommand(ba, BankAccountAbstractCommand.ActionEnum.DEPOSIT, 100)
    cmd.invoke()
    print('After $100 deposit:', ba)
    cmd.undo()
    print('$100 deposit undone:', ba)
    illegal_cmd = BankAccountAbstractCommand(ba, BankAccountAbstractCommand.ActionEnum.WITHDRAW, 1000)
    illegal_cmd.invoke()
    print('After impossible withdrawal:', ba)
    illegal_cmd.undo()
    print('After undo:', ba)

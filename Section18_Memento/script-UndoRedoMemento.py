from Section18_Memento.UndoRedoMemento.BankAccount import BankAccount

if __name__ == '__main__':
    ba = BankAccount(100)
    ba.deposit(50)
    ba.deposit(25)
    print(ba)
    ba.undo()
    print(f'Undo 1: {ba}')
    ba.undo()
    print(f'Undo 2: {ba}')
    ba.redo()
    print(f'Redo 1: {ba}')

from Section18_Memento.RegularMemento.BankAccount import BankAccount

if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)
    # restore to m1
    ba.restore(m1)
    print(ba)
    # restore to m2
    ba.restore(m2)
    print(ba)

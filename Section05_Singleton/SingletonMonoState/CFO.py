from Section05_Singleton.SingletonMonoState.Monostate import Monostate


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}bn'

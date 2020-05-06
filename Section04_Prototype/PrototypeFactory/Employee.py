from Section04_Prototype.PrototypeFactory.Address import Address


class Employee:
    def __init__(self, name, address: Address):
        self.address: Address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'

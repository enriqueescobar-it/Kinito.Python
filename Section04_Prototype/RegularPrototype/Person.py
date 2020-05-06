from Section04_Prototype.RegularPrototype.Address import Address


class Person:
    def __init__(self, name, address: Address):
        self.name = name
        self.address: Address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

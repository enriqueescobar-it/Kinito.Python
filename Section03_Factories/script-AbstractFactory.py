from Section03_Factories.AbstractFactory.CoffeeFactory import CoffeeFactory
from Section03_Factories.AbstractFactory.HotDrinkMachine import HotDrinkMachine
from Section03_Factories.AbstractFactory.TeaFactory import TeaFactory


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()

from Section03_Factories.AbstractFactory.Coffee import Coffee
from Section03_Factories.AbstractFactory.HotDrinkFactory import HotDrinkFactory


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()

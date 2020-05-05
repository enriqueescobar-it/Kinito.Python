from Section03_Factories.AbstractFactory.HotDrinkFactory import HotDrinkFactory
from Section03_Factories.AbstractFactory.Tea import Tea


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()

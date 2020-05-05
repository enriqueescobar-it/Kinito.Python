from Section03_Factories.AbstractFactory.HotDrink import HotDrink


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

from Section03_Factories.AbstractFactory.HotDrink import HotDrink


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')

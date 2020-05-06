from Section03_Factories.FactoryMethod.CoordinateSystemEnum import CoordinateSystemEnum
from Section03_Factories.FactoryMethod.Point import Point


# take out factory methods to a separate class
from Section03_Factories.FactoryMethod.PointFactory import PointFactory

if __name__ == '__main__':
    p1 = Point(2, 3, CoordinateSystemEnum.CARTESIAN)
    p2 = PointFactory.new_cartesian_point(1, 2)
    # or you can expose factory through the type
    p3 = Point.Factory.new_cartesian_point(5, 6)
    p4 = Point.factory.new_cartesian_point(7, 8)
    print(p1, p2, p3, p4)

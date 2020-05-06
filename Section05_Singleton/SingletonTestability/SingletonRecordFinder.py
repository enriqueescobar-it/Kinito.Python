from Section05_Singleton.SingletonTestability.Database import Database


class SingletonRecordFinder:
    def total_population(self, cities: []):
        return sum(Database().population[city] for city in cities)

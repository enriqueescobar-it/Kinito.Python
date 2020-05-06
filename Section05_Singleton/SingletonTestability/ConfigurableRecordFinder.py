class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities: []):
        return sum(self.db.population[city] for city in cities)

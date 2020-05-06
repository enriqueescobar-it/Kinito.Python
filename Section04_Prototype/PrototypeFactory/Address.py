class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'

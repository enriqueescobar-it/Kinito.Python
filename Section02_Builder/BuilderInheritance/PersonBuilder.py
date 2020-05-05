from Section02_Builder.BuilderInheritance.Person import Person


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

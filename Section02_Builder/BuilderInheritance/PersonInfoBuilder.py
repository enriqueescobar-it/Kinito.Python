from Section02_Builder.BuilderInheritance.PersonBuilder import PersonBuilder


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

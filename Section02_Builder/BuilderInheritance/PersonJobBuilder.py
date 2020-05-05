from Section02_Builder.BuilderInheritance.PersonInfoBuilder import PersonInfoBuilder


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

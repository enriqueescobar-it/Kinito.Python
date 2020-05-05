from Section02_Builder.BuilderInheritance.PersonJobBuilder import PersonJobBuilder


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

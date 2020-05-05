from Section02_Builder.BuilderFacets.PersonAddressBuilder import PersonAddressBuilder
from Section02_Builder.BuilderFacets.PersonJobBuilder import PersonJobBuilder
from Section02_Builder.BuilderFacets.Person import Person


class PersonBuilder:  # facade
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

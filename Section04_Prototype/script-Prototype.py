import copy

from Section04_Prototype.RegularPrototype.Address import Address
from Section04_Prototype.RegularPrototype.Person import Person

john = Person("John", Address("123 London Road", "London", "UK"))
print(john)
# jane = john
jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(john, jane)

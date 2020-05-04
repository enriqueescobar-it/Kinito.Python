from Section01_SOLID.Person import Person
from Section01_SOLID.Relationships import Relationships
from Section01_SOLID.Research import Research

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

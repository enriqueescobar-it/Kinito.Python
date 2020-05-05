from Section01_SOLID.DependencyInversionPrinciple.Person import Person
from Section01_SOLID.DependencyInversionPrinciple.Relationships import Relationships
from Section01_SOLID.DependencyInversionPrinciple.Research import Research

parent: Person = Person('John')
child1: Person = Person('Chris')
child2: Person = Person('Matt')

# low-level module
relationships: Relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

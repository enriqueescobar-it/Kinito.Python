from Section01_SOLID.DependencyInversionPrinciple.Relationship import Relationship
from Section01_SOLID.DependencyInversionPrinciple.RelationshipBrowser import RelationshipBrowser


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

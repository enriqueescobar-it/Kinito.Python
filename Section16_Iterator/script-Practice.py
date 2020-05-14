from unittest import *

from Section16_Iterator.Practice.Node import Node


class Evaluate(TestCase):
    def test_exercise(self):
        node = Node('a',
                    Node('b',
                         Node('c'),
                         Node('d')),
                    Node('e'))
        self.assertEqual(
            'abcde',
            ''.join([x for x in node.traverse_preorder()])
        )

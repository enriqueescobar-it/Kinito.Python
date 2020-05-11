from Section13_ChainOfResponsability.Practice.Goblin import Goblin
from Section13_ChainOfResponsability.Practice.WhatToQuery import WhatToQuery


class GoblinKing(Goblin):

    def __init__(self, game):
        super().__init__(game, 3, 3)

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)

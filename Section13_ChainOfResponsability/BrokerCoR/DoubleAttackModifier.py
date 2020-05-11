from Section13_ChainOfResponsability.BrokerCoR.AbstractCreatureModifier import AbstractCreatureModifier
from Section13_ChainOfResponsability.BrokerCoR.WhatToQueryEnum import WhatToQueryEnum


class DoubleAttackModifier(AbstractCreatureModifier):

    def handle(self, sender, query):
        if (sender.name == self.creature.name and
                query.what_to_query == WhatToQueryEnum.ATTACK):
            query.value *= 2

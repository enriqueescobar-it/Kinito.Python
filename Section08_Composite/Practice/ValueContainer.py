from abc import ABC
from typing import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:
                result += i
        return result

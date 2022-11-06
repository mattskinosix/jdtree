from typing import List
from numbers import Number


class Operator:

    def beetween(self, x: Number, y: List[Number]):
        if len(y) != 2:
            return False
        return eval(f'{y[0]} <= {x} <= {y[1]}')

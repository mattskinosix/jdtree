from typing import List
from numbers import Number


class Operator:

    def between(self, x: Number, y: str):
        list = y.split(',')
        if len(list) != 2:
            return False
        return eval(f'{list[0]} <= {x} <= {list[1]}')

    def not_between(self, x: Number, y: str):
        list = y.split(',')
        if len(list) != 2:
            return False
        return not eval(f'{list[0]} <= {x} <= {list[1]}')

from typing import List, Any
from numbers import Number
from distutils.util import strtobool

class Operator:

    def between(self, x: Number, y: str):
        list = y.split(',')
        if len(list) != 2:
            return False
        return list[0] <= x <= list[1]

    def not_between(self, x: Number, y: str):
        list = y.split(',')
        if len(list) != 2:
            return False
        return not list[0] <= {x} <= list[1]

    def empty(self, x: Any, y: str):

        if not x and strtobool(y):
            return True

        if x and not strtobool(y):
            return True

        return False
    
    def greater(self, x: Any, y: str):
        return x > y
    
    def less(self, x: Any, y: str):
        return x < y

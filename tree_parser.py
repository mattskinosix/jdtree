from io import UnsupportedOperation
import json
import logging
from condition import Operator
from constants import OPERATOR, VALUE, VARIABLE


class TreeParser():
    decision = []

    """Docstring for TreeParser. """

    def __init__(self, file_path: str = "test.json"):
        f = open(file_path)
        self.tree = json.load(f)
        self.operation = Operator()

    def decide(self, attribute_to_match):
        return self.__decide_next_node_BSC(attribute_to_match, self.tree)

    def __decide_next_node_BSC(self, attribute_to_match, nodes: dict):
        '''
        Start BSC recursion in the tree.

                Parameters:
                        node (dict): decision tree node
                        object (dict): Object to mach
                Returns:
                        decision (list): list of decisions meet in tree
        '''
        for node in nodes['children']:
            if 'children' not in node.keys():
                self.decision.append(node)
                break
            if self.__compute_condition(node, attribute_to_match):
                self.__decide_next_node_BSC(attribute_to_match, node)
        return self.decision

    def __compute_condition(self, node: dict, attribute_to_match: dict) -> bool:
        '''
        Returns evals of the condition in the three.

                Parameters:
                        node (dict): decision tree node
                        object (dict): Object to mach
                Returns:
                        condition_result (bool): il condition in node is mached
                        by value in object
        '''
        operator = node[OPERATOR]
        variable_name = node[VARIABLE]
        variable_value = node[VALUE]
        target_value = attribute_to_match[variable_name]
        try:
            operation = getattr(self.operation, operator)
            return operation(target_value, variable_value)
        except AttributeError:
            logging.exception('error')
        try:
            return eval(f"{target_value} {operator} {variable_value}")
        except SyntaxError:
            raise UnsupportedOperation(f"{operator} not supported")

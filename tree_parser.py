from io import UnsupportedOperation
from concurrent.futures import ThreadPoolExecutor
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

    def decide(self, attributes_to_match):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for tree in self.tree['leafs']:
                futures.append(executor.submit(
                    self.__decide_next_node_BSC,
                    attributes_to_match,
                    tree,
                    self.tree['variable']
                ))
            results = []
            for future in futures:
                result = future.result()
                if len(result):
                    results.append(result.pop(0))
            return results

    def __decide_next_node_BSC(
            self,
            attributes_to_match,
            node: dict,
            variable: str
    ):
        '''
        Start BSC recursion in the tree.

                Parameters:
                        node (dict): decision tree node
                        object (dict): Object to mach
                Returns:
                        decision (list): list of decisions meet in tree
        '''
        if 'result' in node.keys():
            self.decision.append(node)
        elif self.__compute_condition(
                node,
                attributes_to_match,
                variable
            ):
            for inner_node in node['leafs']:
                self.__decide_next_node_BSC(
                    attributes_to_match,
                    inner_node,
                    node.get(VARIABLE, '')
                )
        return self.decision

    def __compute_condition(
            self,
            node: dict,
            attribute_to_match: dict,
            variable_name: str
    ) -> bool:
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
        variable_value = node[VALUE]
        target_value = attribute_to_match[variable_name]
        try:
            operation = getattr(self.operation, operator)
            return operation(target_value, variable_value)
        except AttributeError:
            pass
        try:
            print(f"{target_value} {operator} {variable_value}")
            return eval(f"{target_value} {operator} {variable_value}")
        except SyntaxError:
            raise UnsupportedOperation(f"{operator} not supported")

from io import UnsupportedOperation
from concurrent.futures import ThreadPoolExecutor
import json
import logging
from .condition import Operator
from .constants import NUMBER_TYPE, OBJECT_TYPE, OPERATOR, STRING_TYPE, TO_PYTHON_TYPE, VALUE, VARIABLE, VARIABLE_TYPE


class JDTEngine():
    decision = []

    """Docstring for TreeParser. """

    def __init__(self, file_path: str = "test.json"):
        f = open(file_path)
        self.tree = json.load(f)['root']
        self.operation = Operator()

    def decide(self, attributes_to_match):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for tree in self.tree['leafs']:
                futures.append(executor.submit(
                    self.__decide_next_node_BSC,
                    attributes_to_match,
                    tree,
                    self.tree[VARIABLE],
                    self.tree[VARIABLE_TYPE]
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
            variable: str,
            variable_type: str
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
                variable,
                variable_type
        ):
            for inner_node in node['leafs']:
                self.__decide_next_node_BSC(
                    attributes_to_match,
                    inner_node,
                    node.get(VARIABLE, ''),
                    node.get(VARIABLE_TYPE, '')
                )

        return self.decision

    def __compute_condition(
            self,
            node: dict,
            attribute_to_match: dict,
            variable_name: str,
            variable_type: str
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
            eval_string = self.get_eval_string(
                variable_type, target_value, operator, variable_value)
            print(eval_string)
            result = eval(eval_string)
            if result:
                logging.info(
                    f"TRUE {variable_type}('{target_value}') {operator} {variable_type}('{variable_value}')")
            return result
        except SyntaxError:
            raise UnsupportedOperation(f"{operator} not supported")

    def get_eval_string(self, variable_type, target_value, operator, variable_value) -> str:

        variable_type_python = TO_PYTHON_TYPE.get(variable_type)
        if variable_type == STRING_TYPE or variable_type == NUMBER_TYPE:
            return f"{variable_type_python}('{target_value}') {operator} {variable_type_python}('{variable_value}')"
        if variable_type == OBJECT_TYPE:
            return f"{target_value} {operator} {variable_value}"

        raise Exception

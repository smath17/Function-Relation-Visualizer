from typing import List

from src.FunctionNode import FunctionNode


# Find and add relations as references to other functions
def add_relations(functions: List[FunctionNode]):
    for function in functions:
        for parameter in function.parameters:
            function.relations = [func for func in functions if func.name.__eq__(parameter)]

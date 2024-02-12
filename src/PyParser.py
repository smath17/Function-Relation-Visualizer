import ast
from _ast import FunctionDef

from src.FunctionNode import FunctionNode


def map_func_to_simple(function: FunctionDef):
    name = function.name
    parameters = [par.arg for par in function.args.args]
    return FunctionNode(name, parameters)


def parse(path):
    with open(path) as file:
        source_tree = ast.parse(file.read())

    functions = [node for node in ast.walk(source_tree) if isinstance(node, ast.FunctionDef)]
    simple_functions = list(map(map_func_to_simple, functions))
    return simple_functions

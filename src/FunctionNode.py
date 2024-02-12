from typing import List


# Simple representation of a function
class FunctionNode:
    def __init__(self, name: str, parameters: List[str], tier=None):
        self.name = name
        self.parameters = parameters
        self.relations: List[FunctionNode] = []
        self.tier = tier
        # Not sure what this is for
        # self.returnValue = returnValue

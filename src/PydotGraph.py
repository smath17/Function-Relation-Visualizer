from typing import List

import pydot

from src.FunctionNode import FunctionNode


def visualize(functions: List[FunctionNode]):
    graph = pydot.Dot("relations_graph", graph_type="graph", bgcolor="white")

    # Add nodes
    for function in functions:
        node = pydot.Node(function.name, label=function.name)
        graph.add_node(node)

    # Create edges
    for function in functions:
        for related_function in function.relations:
            edge = pydot.Edge(function.name, related_function.name)
            graph.add_edge(edge)

    return graph


def save_graph(graph: pydot.Dot):
    graph.write_png("graph.png")

import sys

from src.PyParser import parse
from src.PydotGraph import visualize, save_graph
from src.RelationsMapper import add_relations


def main(path):
    # Parse Python input file
    functions = parse(path)
    # Identify relationships
    add_relations(functions)
    # Visualize graph
    graph = visualize(functions)
    # Export graph
    save_graph(graph)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception(f"Too many arguments. Expected 1, received {str(len(sys.argv) - 1)}")

    path = sys.argv[1]
    if not path[-3:].__eq__(".py"):
        raise Exception("Input file not a Python file")

    main(path)

# TODO: Trim trailing _, remove tier from name (add as member)
# TODO: Create relations based on base name (without tier or trailing _)
# TODO: Match tiers, tier1 can only be used with other tier1's
# TODO: Add loose ends
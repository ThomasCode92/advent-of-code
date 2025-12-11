from sys import stdin


def parse_input(input):
    """
    Parse device connections into a graph
    Each line: device_name: output1 output2 ...
    Returns a dictionary mapping device names to lists of connected devices
    """
    graph = {}
    for line in input.splitlines():
        parts = line.split(": ")
        device = parts[0]
        outputs = parts[1].split() if len(parts) > 1 else []
        graph[device] = outputs
    return graph


def count_paths(graph, start, end, visited=None):
    """
    Count all paths from start to end using DFS
    Tracks visited nodes to avoid cycles
    """
    if visited is None:
        visited = set()

    # Base case: reached the end
    if start == end:
        return 1

    # Avoid cycles
    if start in visited:
        return 0

    # Node not in graph (dead end)
    if start not in graph:
        return 0

    # Mark current node as visited
    visited.add(start)

    # Count paths through all outputs
    total_paths = 0
    for output in graph[start]:
        total_paths += count_paths(graph, output, end, visited)

    # Backtrack: unmark node to allow it in other paths
    visited.remove(start)

    return total_paths


def solve_puzzle_1(graph):
    """
    Find all paths from 'you' to 'out'
    """
    return count_paths(graph, "you", "out")


def solve_puzzle_2(graph):
    """
    Part 2 - to be determined after part 1 is solved
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

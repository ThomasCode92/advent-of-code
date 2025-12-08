from sys import stdin


def parse_input(input):
    """
    Parse 3D coordinates of junction boxes
    Returns a list of tuples (x, y, z)
    """
    lines = input.strip().splitlines()
    boxes = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        boxes.append((x, y, z))
    return boxes


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure
    Tracks which junction boxes are in the same circuit
    """

    def __init__(self, n):
        # Each box starts in its own circuit
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find the root/representative of x's circuit with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Connect two junction boxes into the same circuit
        Returns True if they were in different circuits, False if already connected
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same circuit

        # Union by rank - attach smaller tree under root of larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def get_circuit_sizes(self):
        """
        Count the size of each circuit
        Returns a list of circuit sizes
        """
        circuit_members = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in circuit_members:
                circuit_members[root] = []
            circuit_members[root].append(i)

        return [len(members) for members in circuit_members.values()]


def calculate_distance(box1, box2):
    """Calculate 3D Euclidean distance between two junction boxes"""
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


def solve_puzzle_1(boxes, num_attempts=1000):
    """
    Connect the closest pairs of junction boxes using a greedy algorithm
    After attempting num_attempts connections, find the product of the three largest circuits

    Algorithm:
    1. Calculate all pairwise distances
    2. Sort pairs by distance (shortest first)
    3. Use Union-Find to track circuits
    4. Try to connect pairs in order (may skip if already connected)
    5. After num_attempts tried, count circuit sizes
    6. Return product of three largest circuits

    Note: num_attempts is the number of connections to TRY, not the number
    of successful connections. Some attempts may fail if boxes are already connected.
    """
    n = len(boxes)

    # Calculate all pairwise distances with box indices
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))

    # Sort by distance (shortest first)
    distances.sort()

    # Use Union-Find to track circuits
    uf = UnionFind(n)

    # Try to connect the closest pairs
    for attempt in range(num_attempts):
        if attempt >= len(distances):
            break
        dist, i, j = distances[attempt]
        uf.union(i, j)  # May or may not succeed (already connected)

    # Count circuit sizes
    circuit_sizes = uf.get_circuit_sizes()

    # Sort to find three largest
    circuit_sizes.sort(reverse=True)

    # Multiply three largest (pad with 1s if fewer than 3 circuits)
    result = 1
    for i in range(min(3, len(circuit_sizes))):
        result *= circuit_sizes[i]

    return result


def solve_puzzle_2(boxes):
    """
    Part 2 not yet available
    """
    return None


if __name__ == "__main__":
    input = stdin.read().strip()
    boxes = parse_input(input)

    result_1 = solve_puzzle_1(boxes)
    result_2 = solve_puzzle_2(boxes)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

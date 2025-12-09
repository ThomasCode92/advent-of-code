from sys import stdin


def parse_input(input):
    """
    Parse coordinates of red tiles in the movie theater floor
    Returns a list of tuples (x, y)
    """
    tiles = []
    for line in input.splitlines():
        x, y = map(int, line.split(","))
        tiles.append((x, y))
    return tiles


def solve_puzzle_1(tiles):
    """
    Find the largest rectangle area using any two red tiles as opposite corners
    
    Algorithm:
    1. Try all pairs of red tiles as potential opposite corners
    2. For each pair, calculate the rectangle area (inclusive counting)
    3. Area = (|x2-x1|+1) * (|y2-y1|+1) since we count tiles inclusively
    4. Return the maximum area found
    """
    max_area = 0

    # Check all pairs of tiles
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            # Calculate rectangle area (inclusive of both corners)
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            max_area = max(max_area, area)

    return max_area


def solve_puzzle_2(tiles):
    """
    Placeholder for part 2 - will be revealed after completing part 1
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

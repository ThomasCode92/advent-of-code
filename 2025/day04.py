from sys import stdin

# Directions: 8 adjacent positions (N, NE, E, SE, S, SW, W, NW)
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def parse_input(input):
    """
    Parse grid of paper rolls
    '@' marks paper roll, '.' marks empty space
    """
    grid = []
    for line in input.splitlines():
        grid.append(list(line))
    return grid


def count_adjacent_papers(grid, r, c):
    """
    Count the number of adjacent paper rolls at position (r, c)
    """
    rows = len(grid)
    cols = len(grid[0])
    adjacent_papers = 0

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                adjacent_papers += 1

    return adjacent_papers


def find_accessible_rolls(grid):
    """
    Find all rolls that can be accessed by a forklift
    A roll is accessible if it has fewer than 4 adjacent rolls
    Returns list of (row, col) tuples
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible_rolls = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                if count_adjacent_papers(grid, r, c) < 4:
                    accessible_rolls.append((r, c))

    return accessible_rolls


def solve_puzzle_1(grid):
    """
    Count rolls of paper that can be accessed by a forklift
    A roll is accessible if it has fewer than 4 rolls in adjacent positions
    """
    return len(find_accessible_rolls(grid))


def solve_puzzle_2(grid):
    """
    Simulate removing accessible rolls repeatedly until no more can be removed
    Each time a roll is removed, new rolls may become accessible
    Return the total number of rolls removed
    """
    total_removed = 0

    # Keep removing until no more rolls are accessible
    while True:
        accessible_rolls = find_accessible_rolls(grid)

        # If no accessible rolls found, we're done
        if not accessible_rolls:
            break

        # Remove all accessible rolls
        for r, c in accessible_rolls:
            grid[r][c] = "."

        total_removed += len(accessible_rolls)

    return total_removed


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

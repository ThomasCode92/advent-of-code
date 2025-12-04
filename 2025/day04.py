from sys import stdin


def parse_input(input):
    """
    Parse grid of paper rolls
    '@' marks paper roll, '.' marks empty space
    """
    grid = []
    for line in input.splitlines():
        grid.append(list(line))
    return grid


def solve_puzzle_1(grid):
    """
    Count rolls of paper that can be accessed by a forklift
    A roll is accessible if it has fewer than 4 rolls in adjacent positions
    Return the count of accessible rolls
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    # Directions: 8 adjacent positions (N, NE, E, SE, S, SW, W, NW)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                # Count adjacent paper rolls
                adjacent_papers = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            adjacent_papers += 1

                # Accessible if fewer than 4 adjacent papers
                if adjacent_papers < 4:
                    accessible_count += 1

    return accessible_count


def solve_puzzle_2(grid):
    """
    Placeholder for puzzle 2
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

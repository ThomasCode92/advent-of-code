def find_start_pos(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)  # (col, row)


def parse_input(input):
    grid = [list(row) for row in input.strip().split("\n")]
    start_pos = find_start_pos(grid)
    return grid, start_pos


def patrol(grid, pos):
    idx = 0

    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))  # Up, Right, Down, Left
    rows, cols = len(grid), len(grid[0])

    visited = set()
    visited.add((pos[0], pos[1]))

    while True:
        cur_dir = directions[idx]
        new_pos = (pos[0] + cur_dir[0], pos[1] + cur_dir[1])

        if new_pos[0] < 0 or new_pos[0] >= cols or new_pos[1] < 0 or new_pos[1] >= rows:
            return visited

        if grid[new_pos[1]][new_pos[0]] == "#":
            idx = (idx + 1) % 4
            continue
        else:
            visited.add((new_pos))
            pos = new_pos


def solve_puzzle_1(grid, start_pos):
    visited = patrol(grid, start_pos)
    return len(visited)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)

    print("result for puzzle 1:", result_1)

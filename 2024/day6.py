import json


def find_start_pos(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)  # (col, row)


def parse_input(input):
    grid = [list(row) for row in input.strip().split("\n")]
    start_pos = find_start_pos(grid)
    return grid, start_pos


def patrol(grid, pos, idx=0):
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))  # Up, Right, Down, Left
    rows, cols = len(grid), len(grid[0])

    visited = set()
    visited.add((pos[0], pos[1]))
    visited_entry = {}  # (pos, idx) -> (prev_pos, prev_idx)

    while True:
        cur_dir = directions[idx]
        new_pos = (pos[0] + cur_dir[0], pos[1] + cur_dir[1])

        if new_pos[0] < 0 or new_pos[0] >= cols or new_pos[1] < 0 or new_pos[1] >= rows:
            return True, visited, visited_entry

        if grid[new_pos[1]][new_pos[0]] == "#":
            idx = (idx + 1) % 4
            continue
        else:
            visited.add((new_pos))
            if new_pos not in visited_entry:
                visited_entry[new_pos] = (pos, idx)
            elif visited_entry[new_pos] == (pos, idx):
                return False, None, None  # Loop detected
            pos = new_pos


def solve_puzzle_1(grid, start_pos):
    is_leaving, visited, visited_entry = patrol(grid, start_pos)
    return len(visited)


def solve_puzzle_2(grid, start_pos):
    grid_dump = json.dumps(grid)
    is_leaving, visited, visited_entry = patrol(grid, start_pos)

    visited.remove(start_pos)  # avoid the start position

    loop_count = 0
    for vx, vy in visited:
        grid_copy = json.loads(grid_dump)
        pos, idx = visited_entry[(vx, vy)]

        grid_copy[vy][vx] = "#"  # block the current position
        is_leaving_copy, visited_copy, visited_entry_copy = patrol(
            grid_copy, pos, idx)
        if not is_leaving_copy:  # not leaving, because of the loop
            loop_count += 1
    return loop_count


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)
    result_2 = solve_puzzle_2(*data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

def parse_input(input):
    top_map = [list(map(int, line)) for line in input.splitlines()]
    rows, cols = len(top_map), len(top_map[0])
    return top_map, rows, cols


def find_dest(map, y, x, rows, cols):
    curr = map[y][x]
    next = curr + 1

    endpoints = []
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < rows and 0 <= nx < cols and map[ny][nx] == next:
            if next == 9:
                endpoints.append((ny, nx))
            else:
                endpoints.extend(find_dest(map, ny, nx, rows, cols))
    return endpoints


def solve_puzzle_1(map, rows, cols):
    num = 0
    for y in range(rows):
        for x in range(cols):
            if map[y][x] == 0:
                dest = find_dest(map, y, x, rows, cols)
                num += len(set(dest))
    return num


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)

    print("result for puzzle 1:", result_1)

from collections import defaultdict


def parse_input(input):
    return [list(line) for line in input.split("\n")]


def find_antennas(map):
    rows, cols = len(map), len(map[0])

    antennas = defaultdict(list)
    for row in range(rows):
        for col in range(cols):
            if map[row][col] != ".":
                antennas[map[row][col]].append((row, col))
    return antennas


def solve_puzzle_1(map):
    rows, cols = len(map), len(map[0])
    antennas = find_antennas(map)

    antinodes = set()
    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                for idx, dir in [(i, -1), (j, 1)]:
                    pos = tuple(
                        [a + b * dir for a, b in zip(coords[idx], diff)])
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        antinodes.add(pos)
    return len(antinodes)


def solve_puzzle_2(map):
    rows, cols = len(map), len(map[0])
    antennas = find_antennas(map)

    antinodes = set()
    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                for idx, dir in [(i, -1), (j, 1)]:
                    pos = coords[idx]
                    while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        antinodes.add(pos)
                        pos = tuple(
                            [a + b * dir for a, b in zip(pos, diff)])
    return len(antinodes)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

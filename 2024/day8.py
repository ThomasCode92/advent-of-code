from collections import defaultdict


def parse_input(input):
    return [list(line) for line in input.split("\n")]


def solve_puzzle_1(map):
    rows, cols = len(data), len(data[0])
    antennas = defaultdict(list)
    antinodes = set()

    for row in range(rows):
        for col in range(cols):
            if map[row][col] != ".":
                antennas[map[row][col]].append((row, col))

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                for idx, dir in [(i, -1), (j, 1)]:
                    pos = tuple(
                        [a + b * dir for a, b in zip(coords[idx], diff)])
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        map[pos[0]][pos[1]] = "#"
                        antinodes.add(pos)
    return len(antinodes)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)

    print("result for puzzle 1:", result_1)

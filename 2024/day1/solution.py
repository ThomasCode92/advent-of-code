def parse_line(line):
    numbers = line.split("   ")
    return numbers[0], numbers[1]


def parse_input(input):
    list_1 = []
    list_2 = []

    ids = [parse_line(line) for line in input.splitlines() if line]

    for id in ids:
        list_1.append(id[0])
        list_2.append(id[1])

    list_1.sort()
    list_2.sort()

    return list_1, list_2


def solve_puzzle_1(list_1, list_2):
    sum = 0

    for i in range(len(list_1)):
        diff = int(list_1[i]) - int(list_2[i])
        sum += abs(diff)

    return sum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)

    print("result for puzzle 1:", result_1)

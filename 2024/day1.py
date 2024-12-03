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


def solve_puzzle_2(list_1, list_2):
    sum = 0

    for i in range(len(list_1)):
        num = list_1[i]
        count = list_2.count(num)
        sum += (count * int(list_1[i]))

    return sum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)
    result_2 = solve_puzzle_2(*data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

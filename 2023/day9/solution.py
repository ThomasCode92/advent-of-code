def parse_input(input):
    lines = [line.split(' ') for line in input.splitlines()]
    lines = [list(map(int, line)) for line in lines]
    return lines


def solve_problem_1(lines):
    result = 0
    for line in lines:
        last_number = line[-1]
        not_all_zero = True
        while not_all_zero:
            numbers = []
            for i in range(1, len(line)):
                numbers.append(line[i] - line[i - 1])
            if all(n == 0 for n in numbers):
                not_all_zero = False
            last_number += numbers[-1]
            line = numbers[:]
        result += last_number
    return result


def solve_problem_2(lines):
    result = 0
    for line in lines:
        first_number = line[0]
        not_all_zero = True
        idx = 1
        while not_all_zero:
            numbers = []
            for i in range(1, len(line)):
                numbers.append(line[i] - line[i - 1])
            if all(n == 0 for n in numbers):
                not_all_zero = False
            if idx % 2 != 0:
                first_number -= numbers[0]
            else:
                first_number += numbers[0]
            idx += 1
            line = numbers[:]
        result += first_number
    return result


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(data)
    result_2 = solve_problem_2(data)

    print("result 1:", result_1)
    print("result 2:", result_2)

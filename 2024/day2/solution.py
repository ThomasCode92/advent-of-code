def parse_line(line):
    return [int(num) for num in line.split(' ')]


def parse_input(input):
    return [parse_line(line) for line in input.splitlines() if line]


def is_safe(report):
    diffs = [a - b for a, b in zip(report, report[1:])]
    is_monotonic = all(i > 0 for i in diffs) or all(i < 0 for i in diffs)
    is_in_range = all(1 <= abs(i) <= 3 for i in diffs)
    if is_monotonic and is_in_range:
        return True
    return False


def solve_puzzle_1(reports):
    safe = 0
    for report in reports:
        if is_safe(report):
            safe += 1
    return safe


def solve_puzzle_2(reports):
    safe = 0
    for report in reports:
        if is_safe(report):
            safe += 1
        else:
            for i in range(len(report)):
                tolerated_report = report[:i] + report[i + 1:]
                if is_safe(tolerated_report):
                    safe += 1
                    break
    return safe


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

from sys import stdin
import re


def parse_input(input):
    # Parse comma-separated ranges (e.g., "11-22,95-115")
    ranges = []
    for range_str in input.split(","):
        start, end = range_str.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num):
    # Invalid ID: a sequence of digits repeated exactly twice (e.g., 55, 6464, 123123)
    # No leading zeroes (so 0101 is not valid, but 101 is)
    # Regex: ^([1-9]\d*)\1$ matches a non-zero starting sequence repeated exactly once
    return bool(re.match(r"^([1-9]\d*)\1$", str(num)))


def solve_puzzle_1(ranges):
    # Find all invalid IDs in the given ranges and sum them
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    return total


def solve_puzzle_2(data):
    # TODO: Solve puzzle 2
    pass


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

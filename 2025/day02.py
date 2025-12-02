from sys import stdin
import re


def parse_input(input):
    # Parse comma-separated ranges (e.g., "11-22,95-115")
    ranges = []
    for range_str in input.split(","):
        start, end = range_str.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num, exact=False):
    # Invalid ID: a sequence of digits repeated at least twice
    # No leading zeroes (so 0101 is not valid, but 101 is)
    # exact=True (exactly twice): ^([1-9]\d*)\1$
    # exact=False (at least twice): ^([1-9]\d*)\1+$
    pattern = r"^([1-9]\d*)\1$" if exact else r"^([1-9]\d*)\1+$"
    return bool(re.match(pattern, str(num)))


def solve_puzzle_1(ranges):
    # Find all invalid IDs (repeated exactly twice) in the given ranges and sum them
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num, exact=True):
                total += num

    return total


def solve_puzzle_2(ranges):
    # Find all invalid IDs (repeated at least twice) and sum them
    total = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num, exact=False):
                total += num

    return total


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

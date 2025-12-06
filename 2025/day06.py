from sys import stdin
from functools import reduce
from operator import mul, add


def parse_input(input):
    """
    Parse the math worksheet into columns

    Example:
        123 328  51 64
         45 64  387 23
          6 98  215 314
        *   +   *   +

    Returns: [['123', '45', '6', '*'], ['328', '64', '98', '+'], ...]
    """
    lines = input.splitlines()

    # Split each line on whitespace to get columns
    rows = [line.split() for line in lines]

    # Transpose to get columns (each column is one problem)
    columns = list(map(list, zip(*rows)))

    return columns


def parse_problems(columns):
    """
    Convert columns into problems with numbers and operation functions

    Takes: [['123', '45', '6', '*'], ['328', '64', '98', '+'], ...]
    Returns: [[[123, 45, 6], mul], [[328, 64, 98], add], ...]
    """
    problems = []

    for column in columns:
        operation = mul if "*" in column[-1] else add
        numbers = [int(num_str.strip()) for num_str in column[:-1]]
        problems.append([numbers, operation])

    return problems


def solve_puzzle_1(problems):
    """
    Calculate the grand total by solving each problem and summing the results

    For each problem:
    - Apply the operation to all numbers using reduce
    - Sum all problem results
    """
    grand_total = 0

    for numbers, operation in problems:
        # Apply operation to all numbers: reduce(mul, [2, 3, 4]) = 2*3*4 = 24
        result = reduce(operation, numbers)
        grand_total += result

    return grand_total


def solve_puzzle_2(problems):
    """
    Placeholder for part 2 - will be revealed after solving part 1
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    columns = parse_input(input)
    problems = parse_problems(columns)

    result_1 = solve_puzzle_1(problems)
    result_2 = solve_puzzle_2(problems)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

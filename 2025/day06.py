from functools import reduce
from itertools import zip_longest
from operator import add, mul
from sys import stdin


def parse_input(input):
    """
    Parse the math worksheet by splitting at operator positions.

    The key insight: operators are left-aligned and mark problem boundaries.
    By splitting at these positions, we preserve internal whitespace in numbers,
    which encodes their digit alignment for cephalopod math (Part 2).

    Example:
        123 328  51 64
         45 64  387 23
          6 98  215 314
        *   +   *   +

    Operator positions: [0, 4, 8, 12]

    Problem 0 (split at 0:3):
        '123'  (from line 0)
        ' 45'  (from line 1) - note the leading space
        '  6'  (from line 2) - note the two leading spaces
        '*'    (operator)

    Returns: [[['123', ' 45', '  6'], mul], ...]
    """
    lines = input.splitlines()

    # Find operator positions (non-space characters in last line)
    operator_line = lines[-1]
    pos = [i for i, c in enumerate(operator_line) if c != " "]
    pos.append(len(operator_line) + 1)  # Add end position

    # Split each line at these positions, preserving whitespace
    parsed = []
    for line in lines:
        segments = [line[a : b - 1] for a, b in zip(pos, pos[1:])]
        parsed.append(segments)

    # Convert operators to functions
    parsed[-1] = [mul if "*" in x else add for x in parsed[-1]]

    # Transpose to get problems (each column becomes a problem)
    problems = list(map(list, zip(*parsed)))

    return problems


def align_numbers(numbers):
    """
    Align numbers for cephalopod math by reading digit columns.

    Numbers have whitespace preserved, which encodes alignment:
        '123'  -> digits at positions 0,1,2
        ' 45'  -> digits at positions 1,2 (space at 0)
        '  6'  -> digit at position 2 (spaces at 0,1)

    Using zip_longest:
        Position 0: '1', ' ', ' ' -> "1" -> 1
        Position 1: '2', '4', ' ' -> "24" -> 24
        Position 2: '3', '5', '6' -> "356" -> 356

    Returns: [1, 24, 356]
    """
    aligned_columns = zip_longest(*numbers, fillvalue="")
    return (int("".join(digits)) for digits in aligned_columns)


def solve_puzzle_1(problems):
    """
    Part 1: Simple left-to-right evaluation.

    Parse numbers by stripping whitespace and converting to int.
    Apply operator left-to-right using reduce.
    """
    grand_total = 0

    for problem in problems:
        numbers = [int(num_str.strip()) for num_str in problem[:-1]]
        operation = problem[-1]
        result = reduce(operation, numbers)
        grand_total += result

    return grand_total


def solve_puzzle_2(problems):
    """
    Part 2: Cephalopod math.

    Read numbers by digit columns (using preserved whitespace alignment).
    Apply operator to the resulting numbers.
    """
    grand_total = 0

    for problem in problems:
        number_strings = problem[:-1]
        operation = problem[-1]
        numbers = list(align_numbers(number_strings))
        result = reduce(operation, numbers)
        grand_total += result

    return grand_total


if __name__ == "__main__":
    input = stdin.read().rstrip("\n")  # Remove trailing newlines but preserve spaces
    problems = parse_input(input)

    result_1 = solve_puzzle_1(problems)
    result_2 = solve_puzzle_2(problems)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

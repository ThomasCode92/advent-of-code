from itertools import product


def parse_input(input):
    results, equations = [], []
    for line in input.split("\n"):
        result, numbers = line.split(":")
        results.append(int(result))
        equations.append([int(n) for n in numbers.split()])
    return results, equations


def evaluate_expression(numbers, operators):
    """Evaluates an expression from numbers and operators (left-to-right)."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "|":
            # Concatenate the digits of the two numbers
            result = int(str(result) + str(numbers[i + 1]))
    return result


def solve_calibration(test_values, calibrations, operators="+*"):
    """Finds which equations can be true and calculates the total calibration result."""
    total_calibration = 0
    for i, calibration in enumerate(calibrations):
        test_value = test_values[i]
        n = len(calibration) - 1  # Number of operator slots
        possible = False

        # Try all combinations
        for op in product(operators, repeat=n):
            if evaluate_expression(calibration, op) == test_value:
                possible = True
                break

        if possible:
            total_calibration += test_value
    return total_calibration


def solve_puzzle_1(test_values, calibrations):
    return solve_calibration(test_values, calibrations)


def solve_puzzle_2(test_values, calibrations):
    return solve_calibration(test_values, calibrations, "+*|")


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)
    result_2 = solve_puzzle_2(*data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

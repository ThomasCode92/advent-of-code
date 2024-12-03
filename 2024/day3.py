import re


def extract_mul_instructions(corrupted_memory):
    pattern = r"mul\((\d+),(\d+)\)"
    mul_instructions = re.findall(pattern, corrupted_memory)
    return mul_instructions


def solve_puzzle_1(corrupted_memory):
    mul_instructions = extract_mul_instructions(corrupted_memory)

    sum = 0
    for instruction in mul_instructions:
        a, b = map(int, instruction)
        sum += a * b
    return sum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()

    result_1 = solve_puzzle_1(input)

    print("result for puzzle 1:", result_1)

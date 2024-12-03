import re


def extract_mul_instructions(corrupted_memory, pattern=r"mul\((\d+),(\d+)\)"):
    mul_instructions = re.findall(pattern, corrupted_memory)
    return mul_instructions


def solve_puzzle_1(corrupted_memory):
    mul_instructions = extract_mul_instructions(corrupted_memory)

    sum = 0
    for instruction in mul_instructions:
        a, b = map(int, instruction)
        sum += a * b
    return sum


def solve_puzzle_2(corrupted_memory):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"
    pattern = f"{control_pattern}|{mul_pattern}"

    instructions = extract_mul_instructions(corrupted_memory, pattern=pattern)

    mul_enabled = True  # By default, mul instructions are enabled
    sum = 0

    for instr in instructions:
        if instr[0] == "do()":
            mul_enabled = True
        elif instr[0] == "don't()":
            mul_enabled = False
        elif instr[1] and instr[2] and mul_enabled:
            a, b = int(instr[1]), int(instr[2])
            sum += a * b

    return sum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()

    result_1 = solve_puzzle_1(input)
    result_2 = solve_puzzle_2(input)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

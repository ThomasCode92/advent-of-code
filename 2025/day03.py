from sys import stdin


def parse_input(input):
    # Each line is a bank of batteries with joltage ratings (1-9)
    return input.splitlines()


def solve_puzzle_1(banks):
    # For each bank, find the largest two-digit number by choosing exactly two batteries
    # Batteries maintain their order (cannot rearrange)
    total = 0

    for bank in banks:
        max_joltage = 0
        # Try all pairs of batteries (i, j) where i < j
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                # Form a two-digit number from batteries at positions i and j
                joltage = int(bank[i] + bank[j])
                max_joltage = max(max_joltage, joltage)
        total += max_joltage

    return total


def solve_puzzle_2(data):
    # TODO: Implement puzzle 2 solution
    pass


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

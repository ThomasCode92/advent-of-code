from sys import stdin


def parse_input(input):
    # Each line is a bank of batteries with joltage ratings (1-9)
    return input.splitlines()


def solve_puzzle_1(banks):
    """
    For each bank, find the largest two-digit number by choosing exactly two batteries
    Batteries maintain their order (cannot rearrange)
    """

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


def solve_puzzle_2(banks):
    """
    For each bank, find the largest 12-digit number by choosing exactly 12 batteries
    Strategy: Greedily select batteries to maximize value at each position
    At each position, choose the largest available digit that still allows us to select enough remaining batteries
    """

    total = 0

    for bank in banks:
        n = len(bank)
        batteries_needed = 12
        selected = []
        i = 0

        # Greedily select the largest digit at each step
        while len(selected) < batteries_needed:
            # How many more batteries do we need after this one?
            remaining_needed = batteries_needed - len(selected) - 1
            # How far ahead can we look? We need to leave enough batteries for the rest
            max_index = n - remaining_needed

            # Find the largest digit in the range [i, max_index)
            best_digit = "0"
            best_index = i
            for j in range(i, max_index):
                if bank[j] > best_digit:
                    best_digit = bank[j]
                    best_index = j

            selected.append(best_digit)
            i = best_index + 1

        joltage = int("".join(selected))
        total += joltage

    return total


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

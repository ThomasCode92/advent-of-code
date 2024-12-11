def parse_input(input):
    return input.split(" ")


def flatten_list(lst):
    return [item for sublist in lst for item in sublist]


def transform_stone(number):
    # Rule 1: If the number is 0, replace with a stone engraved with 1.
    if number == 0:
        return [1]

    num_str = str(number)
    # Rule 2: If the number has an even number of digits, split it into two stones.
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left_half = int(num_str[:mid])  # Convert left half to integer
        right_half = int(num_str[mid:])  # Convert right half to integer
        return [left_half, right_half]

    # Rule 3: If none of the other rules apply, replace the stone with one engraved with the number * 2024.
    return [number * 2024]


def solve_puzzle_1(data):
    stones = [transform_stone(int(number)) for number in data]
    for _ in range(24):
        stones = [transform_stone(number)
                  for stone in stones for number in stone]

    return len(flatten_list(stones))


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)

    print("result for puzzle 1:", result_1)

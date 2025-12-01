from sys import stdin


def parse_input(input):
    # Parse rotations: each line is direction (L/R) followed by distance
    rotations = []
    for line in input.splitlines():
        direction = line[0]
        distance = int(line[1:])
        rotations.append((direction, distance))
    return rotations


def solve_puzzle_1(rotations):
    # Dial starts at 50, count how many times it points to 0 after rotations
    # Dial has numbers 0-99 (100 positions)
    position = 50
    count_zeros = 0

    for direction, distance in rotations:
        if direction == "L":
            # Left moves toward lower numbers (subtract)
            position = (position - distance) % 100
        else:  # direction == 'R'
            # Right moves toward higher numbers (add)
            position = (position + distance) % 100

        if position == 0:
            count_zeros += 1

    return count_zeros


def solve_puzzle_2(rotations):
    # Count every time any click causes the dial to point at 0
    position = 50
    count_zeros = 0

    for direction, distance in rotations:
        # Calculate distance to reach 0 from current position
        if position == 0:
            distance_to_zero = 100
        elif direction == "L":
            distance_to_zero = position
        else:  # direction == "R"
            distance_to_zero = 100 - position

        # Count complete loops (every 100 clicks passes through 0)
        hits = distance // 100
        # Check if partial rotation reaches 0
        if distance % 100 >= distance_to_zero:
            hits += 1

        count_zeros += hits
        position = (
            position - distance if direction == "L" else position + distance
        ) % 100

    return count_zeros


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

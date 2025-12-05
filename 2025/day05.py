from sys import stdin


def parse_input(input):
    """
    Parse the database file with fresh ingredient ID ranges and available IDs
    Returns tuple of (ranges, available_ids)
    - ranges: list of tuples (start, end) representing inclusive ranges
    - available_ids: list of ingredient IDs to check
    """
    parts = input.split("\n\n")

    # Parse fresh ID ranges
    ranges = []
    for line in parts[0].strip().splitlines():
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    # Parse available ingredient IDs
    available_ids = []
    for line in parts[1].strip().splitlines():
        available_ids.append(int(line))

    return ranges, available_ids


def is_fresh(ingredient_id, ranges):
    """
    Check if an ingredient ID is fresh (falls within any range)
    Ranges are inclusive on both ends
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def solve_puzzle_1(ranges, available_ids):
    """
    Count how many of the available ingredient IDs are fresh
    An ID is fresh if it falls into any of the fresh ID ranges
    """
    fresh_count = 0
    for ingredient_id in available_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
    return fresh_count


def solve_puzzle_2(ranges, available_ids):
    """
    Placeholder for puzzle 2 - will be revealed after solving puzzle 1
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    ranges, available_ids = parse_input(input)

    result_1 = solve_puzzle_1(ranges, available_ids)
    result_2 = solve_puzzle_2(ranges, available_ids)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

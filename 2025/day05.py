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
    Count total number of unique ingredient IDs considered fresh by the ranges
    Ranges can overlap, so we need to merge them to avoid double counting
    For example: ranges 3-5, 10-14, 16-20, 12-18
    Covers: 3,4,5,10,11,12,13,14,15,16,17,18,19,20 = 14 IDs
    """

    # Sort ranges by start position
    sorted_ranges = sorted(ranges)

    # Merge overlapping ranges
    merged_ranges = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        # If current range overlaps or is adjacent to last range, merge them
        if start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged_ranges.append((start, end))

    # Count total IDs in merged ranges
    total_ids = 0
    for start, end in merged_ranges:
        total_ids += end - start + 1

    return total_ids


if __name__ == "__main__":
    input = stdin.read().strip()
    ranges, available_ids = parse_input(input)

    result_1 = solve_puzzle_1(ranges, available_ids)
    result_2 = solve_puzzle_2(ranges, available_ids)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

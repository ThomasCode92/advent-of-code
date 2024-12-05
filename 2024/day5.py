def parse_rules(input):
    rules = []
    for line in input.split("\n"):
        before, after = map(int, line.split('|'))
        rules.append((before, after))
    return rules


def parse_updates(input):
    updates = []
    for line in input.split("\n"):
        updates.append(list(map(int, line.split(','))))
    return updates


def parse_input(input):
    data = input.split("\n\n")
    rules = parse_rules(data[0])
    updates = parse_updates(data[1])
    return rules, updates


def check_update_order(rules, update):
    """Checks if the given update adheres to the ordering rules."""
    # Create a mapping of page positions in the update
    page_positions = {page: idx for idx, page in enumerate(update)}

    # Validate each rule that applies to the update
    for before, after in rules:
        if before in page_positions and after in page_positions:
            if page_positions[before] >= page_positions[after]:
                return False
    return True


def solve_puzzle_1(rules, updates):
    sum = 0
    for i, update in enumerate(updates):
        is_valid = check_update_order(rules, update)
        if is_valid:
            middleIndex = int((len(update) - 1)/2)
            sum += update[middleIndex]
    return sum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(*data)

    print("result for puzzle 1:", result_1)

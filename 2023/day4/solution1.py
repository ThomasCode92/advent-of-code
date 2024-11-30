def parse_part(numbers):
    parsed_numbers = []
    for n in range(0, len(numbers), 3):
        parsed_numbers.append(int(numbers[n + 1: n + 3].strip()))
    return parsed_numbers


def parse_line(line):
    card, numbers = line.split(":")
    card_number = int(card[5:].strip())

    winning_numbers, game_numbers = numbers.split(" |")
    winning_numbers = parse_part(winning_numbers)
    game_numbers = parse_part(game_numbers)

    return (card_number, winning_numbers, game_numbers)


def parse_input(input):
    lines = [parse_line(line) for line in input.splitlines() if line]
    return lines


def solve_problem_1(data):
    sum = 0
    for _, winning_numbers, game_numbers in data:
        matching_numbers = len(set(winning_numbers) & set(game_numbers))
        if matching_numbers > 0:
            sum += 2 ** (matching_numbers - 1)
    return sum


def solve_problem_2(data):
    cards = [1] * len(data)
    for card_number, winning_numbers, game_numbers in data:
        matching_numbers = len(set(winning_numbers) & set(game_numbers))
        for number in range(matching_numbers):
            cards[card_number+number] += cards[card_number-1]
        print(cards)
    return sum(cards)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(data)
    result_2 = solve_problem_2(data)

    print('result 1:', result_1)
    print('result 2:', result_2)

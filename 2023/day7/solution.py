from collections import Counter

# fmt: off
card_dict = {"A": "A", "K": "B", "Q": "C", "J": "D", "T": "E", "9": "F", "8": "G","7": "H", "6": "I", "5": "J", "4": "K", "3": "L", "2": "M"}
hand_dict = {'five_of_a_kind': [], 'four_of_a_kind': [], 'full_house': [], 'three_of_a_kind': [], 'two_pair': [], 'one_pair': [], 'high_card': []}
# fmt: on


def parse_input(input):
    return [line.split() for line in input.splitlines()]


def parse_cards(cards):
    for key, value in card_dict.items():
        cards = cards.replace(key, value)
    card_count = Counter(cards).values()
    return cards, card_count


def reset_hand_dict():
    for key in hand_dict:
        hand_dict[key] = []


def classify_normal_hand(cards, bid, card_count):
    if 5 in card_count:
        hand_dict['five_of_a_kind'].append((cards, bid))
    elif 4 in card_count:
        hand_dict['four_of_a_kind'].append((cards, bid))
    elif (3 in card_count) and (2 in card_count):
        hand_dict['full_house'].append((cards, bid))
    elif (3 in card_count) and (2 not in card_count):
        hand_dict['three_of_a_kind'].append((cards, bid))
    elif Counter(card_count)[2] == 2:
        hand_dict['two_pair'].append((cards, bid))
    elif Counter(card_count)[2] == 1:
        hand_dict['one_pair'].append((cards, bid))
    else:
        hand_dict['high_card'].append((cards, bid))


def classify_joker_hand(cards, bid, card_count):
    if (5 in card_count) or (4 in card_count) or ((3 in card_count) and (2 in card_count)):
        hand_dict['five_of_a_kind'].append((cards, bid))
    elif (3 in card_count) and (2 not in card_count):
        hand_dict['four_of_a_kind'].append((cards, bid))
    elif Counter(card_count)[2] == 2:
        if Counter(cards)['X'] == 2:
            hand_dict['four_of_a_kind'].append((cards, bid))
        elif Counter(cards)['X'] == 1:
            hand_dict['full_house'].append((cards, bid))
    elif Counter(card_count)[2] == 1:
        hand_dict['three_of_a_kind'].append((cards, bid))
    else:
        hand_dict['one_pair'].append((cards, bid))


def calc_winnings(num_of_games):
    total_winnings = 0
    for hand_type in ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']:
        for result in hand_dict[hand_type]:
            total_winnings += int(result[1]) * num_of_games
            num_of_games -= 1
    return total_winnings


def solve_problem_1(games):
    num_of_games = len(games)
    for cards, bid in games:
        cards, cart_count = parse_cards(cards)

        classify_normal_hand(cards, bid, cart_count)

    for _, games in hand_dict.items():
        games.sort(key=lambda a: a[0])

    return calc_winnings(num_of_games)


def solve_problem_2(games):
    reset_hand_dict()
    card_dict['J'] = 'X'
    num_of_games = len(games)

    for cards, bid in games:
        cards, cart_count = parse_cards(cards)

        if 'X' in cards:
            classify_joker_hand(cards, bid, cart_count)
        else:
            classify_normal_hand(cards, bid, cart_count)

    for _, games in hand_dict.items():
        games.sort(key=lambda a: a[0])

    return calc_winnings(num_of_games)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(data)
    result_2 = solve_problem_2(data)

    print("result 1:", result_1)
    print("result 2:", result_2)

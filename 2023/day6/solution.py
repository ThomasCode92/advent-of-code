def parse_input(input):
    lines = input.splitlines()
    times = [int(i) for i in lines[0].split(":")[1].split()]
    dist = [int(i) for i in lines[1].split(":")[1].split()]
    return times, dist


def join_lists(list1, list2):
    number1 = int(''.join([str(x) for x in list1]))
    number2 = int(''.join([str(x) for x in list2]))
    return number1, number2


def cal_winning_races(times, dist):
    winning_races = []
    for idx, time in enumerate(times):
        number = 0
        for t in list(range(time)):
            distance = t * (time-t)
            if distance > dist[idx]:
                number += 1
        winning_races.append(number)
    return winning_races


def solve_problem_1(times, dist):
    number_of_races = cal_winning_races(times, dist)
    sum = 1
    for number in number_of_races:
        sum *= number
    return sum


def solve_problem_2(times, dist):
    total_time, total_dist = join_lists(times, dist)
    return cal_winning_races([total_time], [total_dist])[0]


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(*data)
    result_2 = solve_problem_2(*data)

    print('result 1:', result_1)
    print('result 2:', result_2)

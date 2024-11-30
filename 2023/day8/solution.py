from math import lcm


def parse_input(input):
    lines = [line for line in input.split("\n")]
    lines = [line for line in lines if line != ""]
    lr_instructions = lines[0]
    connections = {}
    for line in lines[1:]:
        destination = line.split('=')[0].strip()
        instructions = line.split('=')[1].strip()[1:-1].split(',')
        connections[destination] = (instructions[0].strip(),
                                    instructions[1].strip())
    return lr_instructions, connections


def solve_problem_1(lr_instructions, connections):
    position = 'AAA'
    idx = 0
    while position != 'ZZZ':
        direction = lr_instructions[idx % len(lr_instructions)]
        position = connections[position][0 if direction == 'L' else 1]
        idx += 1
    return idx


def solve_problem_2(lr_instructions, connections):
    result = 1
    for connection in connections:
        if connection.endswith('A'):
            position = connection
            idx = 0
            while not position.endswith('Z'):
                direction = lr_instructions[idx % len(lr_instructions)]
                position = connections[position][0 if direction == 'L' else 1]
                idx += 1
            result = lcm(result, idx)
    return result


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(*data)
    result_2 = solve_problem_2(*data)

    print("result 1:", result_1)
    print("result 2:", result_2)

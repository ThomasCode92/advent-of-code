def parse_almanac_map(almanac_map):
    almanac_map_info = []
    for line in almanac_map.splitlines()[1:]:
        destination, source, range = list(map(int, line.split()))
        almanac_map_info.append((destination, source, range))
    return almanac_map_info


def parse_input(input):
    seeds, *almanac_maps = input.split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))
    return seeds, almanac_maps


def solve_problem_1(seeds, almanac_maps):
    input = seeds
    for almanac_map in almanac_maps:
        almanac_map_info = parse_almanac_map(almanac_map)
        mapped_input = []
        for input_value in input:
            for destination, source, range in almanac_map_info:
                # check if value is in a mapped range
                if source <= input_value < source + range:
                    offset = destination - source
                    mapped_input.append(input_value + offset)
                    break
            # if not in a mapped range, keep current value
            else:
                mapped_input.append(input_value)
        input = mapped_input
    return min(mapped_input)


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_problem_1(*data)

    print('result 1:', result_1)

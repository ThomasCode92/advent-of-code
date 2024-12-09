def parse_input(input):
    return input


def parse_disk_map(disk_map):
    """Parse the disk map into file and free space segments."""
    segments = []
    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            segments.append(('file', int(char)))
        else:
            segments.append(('free', int(char)))
    return segments


def build_disk_layout(segments):
    """Build the initial disk layout from the parsed segments."""
    layout = []
    num_files = 0
    file_id = 0
    for segment_type, length in segments:
        if segment_type == 'file':
            layout.extend([str(file_id)] * length)
            num_files += length
            file_id += 1
        else:  # Free space
            layout.extend(['.'] * length)
    return layout, num_files


def transform_disk_layout(layout, num_files):
    """Transform the disk layout into the final layout."""
    length = len(layout)
    output = []
    for i, char in enumerate(layout):
        if i == num_files:
            break
        if char != ".":
            output.append(char)
        else:
            j = length - 1
            while layout[j] == ".":
                j -= 1
            output.append(layout[j])
            layout[j] = "."
    return output


def calculate_checksum(layout):
    ints = [int(num) for num in layout]
    checksum = 0
    for i, num in enumerate(ints):
        checksum += num * i
    return checksum


def solve_puzzle_1(string):
    segments = parse_disk_map(string)
    disk_layout, num_files = build_disk_layout(segments)
    transformed_layout = transform_disk_layout(disk_layout, num_files)
    checksum = calculate_checksum(transformed_layout)
    return checksum


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)

    print("result for puzzle 1:", result_1)

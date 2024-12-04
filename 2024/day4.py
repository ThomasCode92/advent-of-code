directions = [
    (0, 1),   # Right
    (1, 0),   # Down
    (1, 1),   # Diagonal down-right
    (1, -1),  # Diagonal down-left
    (0, -1),  # Left
    (-1, 0),  # Up
    (-1, -1),  # Diagonal up-left
    (-1, 1)   # Diagonal up-right
]


def parse_input(input):
    return input.splitlines()


def find_word(x, y, index, dx, dy, grid, rows, cols, word):
    # Base case: if index reaches the word length, we found the word
    if index == len(word):
        return 1
    # Check bounds and if current cell matches the word[index]
    if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[index]:
        return 0
    # Recursively search the next character in the given direction
    return find_word(x + dx, y + dy, index + 1, dx, dy, grid, rows, cols, word)


# Check if the letter is 'A' and the surrounding letters form the pattern 'MAS'
def matches_xmas_pattern(letter, x, y):
    pattern = {"M", "S"}
    if not letter == "A":
        return False
    return {data[x - 1][y - 1], data[x + 1][y + 1]} == pattern and {data[x - 1][y + 1], data[x + 1][y - 1]} == pattern


def solve_puzzle_1(grid):
    word = "XMAS"
    rows, cols = len(grid), len(grid[0])

    total_count = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:  # Start searching only from 'X'
                for dx, dy in directions:
                    total_count += find_word(x, y, 0,
                                             dx, dy, grid, rows, cols, word)
    return total_count


def solve_puzzle_2(data):
    rows, cols = len(data), len(data[0])

    xmas_count = 0
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if matches_xmas_pattern(data[x][y], x, y):
                xmas_count += 1
    return xmas_count


if __name__ == "__main__":
    from sys import stdin

    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(data)
    result_2 = solve_puzzle_2(data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

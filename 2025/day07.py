from sys import stdin


def parse_input(input):
    """
    Parse the tachyon manifold diagram
    Returns a dict with:
    - grid: 2D list of characters
    - start_col: column index where 'S' is located
    - rows: number of rows
    - cols: number of columns
    """
    lines = input.strip().splitlines()
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Find starting column where 'S' is located
    start_col = None
    for c in range(cols):
        if grid[0][c] == "S":
            start_col = c
            break

    return {
        'grid': grid,
        'start_col': start_col,
        'rows': rows,
        'cols': cols
    }


def simulate_beams(grid, start_col, rows, cols):
    """
    Simulate tachyon beams using an array approach
    Array tracks number of beams at each column position
    Returns the total number of splits that occurred

    A split occurs when a splitter is first encountered.
    Multiple beams hitting the same splitter don't create additional splits.
    """
    # Initialize beam array - one beam at starting column
    beams = [0] * cols
    beams[start_col] = 1

    split_count = 0
    split_positions = set()  # Track which splitters have been hit

    # Move the beam array down row by row
    for row in range(rows - 1):  # Stop before last row since beams exit
        next_beams = [0] * cols

        for col in range(cols):
            if beams[col] == 0:
                continue  # No beams at this column

            beam_count = beams[col]
            next_row = row + 1

            # Check what's at the next position
            if grid[next_row][col] == "^":
                # Hit a splitter - only count if first time
                if (next_row, col) not in split_positions:
                    split_positions.add((next_row, col))
                    split_count += 1

                # Split left
                if col > 0:
                    next_beams[col - 1] += beam_count

                # Split right
                if col < cols - 1:
                    next_beams[col + 1] += beam_count
            else:
                # Empty space - beams continue straight down
                next_beams[col] += beam_count

        beams = next_beams

        # Stop if no more beams
        if all(b == 0 for b in beams):
            break

    return split_count


def solve_puzzle_1(grid, start_col, rows, cols):
    """
    Count how many times the tachyon beam is split
    A beam splits when it hits a splitter ('^'), creating two new beams
    """
    return simulate_beams(grid, start_col, rows, cols)


def solve_puzzle_2(grid, start_col, rows, cols):
    """
    Placeholder for puzzle 2 - will be revealed after puzzle 1 is solved
    """
    return 0


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(**data)
    result_2 = solve_puzzle_2(**data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

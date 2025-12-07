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

    return {"grid": grid, "start_col": start_col, "rows": rows, "cols": cols}


def simulate_beams(grid, start_col, rows, cols, track_unique_splits=False):
    """
    Simulate tachyon beams using an array approach
    Array tracks number of beams/timelines at each column position

    If track_unique_splits=True (puzzle 1):
        - Only counts each splitter once (first encounter)
        - Returns the number of unique splitters hit

    If track_unique_splits=False (puzzle 2):
        - Each beam hitting a splitter creates two timelines
        - Returns the total number of timelines at the end
    """
    # Initialize beam array - one beam at starting column
    beams = [0] * cols
    beams[start_col] = 1

    split_count = 0
    split_positions = set()

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
                # Hit a splitter
                if track_unique_splits and (next_row, col) not in split_positions:
                    # Puzzle 1: only count if first time
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

    # Return result based on mode
    if track_unique_splits:
        return split_count
    else:
        return sum(beams)


def solve_puzzle_1(grid, start_col, rows, cols):
    """
    Count how many times the tachyon beam is split
    A beam splits when it hits a splitter ('^'), creating two new beams
    Only counts each splitter once (first encounter)
    """
    return simulate_beams(grid, start_col, rows, cols, track_unique_splits=True)


def solve_puzzle_2(grid, start_col, rows, cols):
    """
    Count the number of unique timelines using many-worlds interpretation
    Each time a particle hits a splitter, it creates two timelines (left and right)
    """
    return simulate_beams(grid, start_col, rows, cols, track_unique_splits=False)


if __name__ == "__main__":
    input = stdin.read().strip()
    data = parse_input(input)

    result_1 = solve_puzzle_1(**data)
    result_2 = solve_puzzle_2(**data)

    print("result for puzzle 1:", result_1)
    print("result for puzzle 2:", result_2)

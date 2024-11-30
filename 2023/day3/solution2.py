# check if entry is a symbol
def is_symbol(i, j):
    # check the boundaries of the matrix
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return False

    # check if the entry is a * symbol
    if lines[i][j] == '*':
        gear_ratios[i][j].append(number)

    # check if the entry is a symbol
    return lines[i][j] != '.' and not lines[i][j].isdigit()


# open file
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    sum = 0

    # number of rows and columns
    rows = len(lines)
    cols = len(lines[0])

    # initialize a 2D list for gear ratios
    gear_ratios = [[[] for _ in range(cols)] for _ in range(rows)]
    gear_ratio = 0

    # loop through each line
    for row_idx, line in enumerate(lines):
        start = col_idx = 0

        # loop through each column to find numbers
        while col_idx < cols:
            start = col_idx
            number = ''

            # make consecutive numbers into one
            while col_idx < cols and line[col_idx].isdigit():
                number += line[col_idx]
                col_idx += 1
            if number == '':
                col_idx += 1
                continue

            # Convert the extracted digits to an integer
            number = int(number)

            # check before and after number
            if is_symbol(row_idx, start - 1) or is_symbol(row_idx, col_idx):
                sum += number
                continue

            # check above and below number
            for k in range(start-1, col_idx+1):
                if is_symbol(row_idx-1, k) or is_symbol(row_idx+1, k):
                    sum += number
                    break

    # calculate gear ratios
    for i in range(rows):
        for j in range(cols):
            ratios = gear_ratios[i][j]
            if lines[i][j] == "*" and len(ratios) == 2:
                gear_ratio += ratios[0] * ratios[1]

    # final result
    print(sum, gear_ratio)

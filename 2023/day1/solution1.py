# read the input-file and log the output
with open('input-1.txt', 'r') as f:
    sum = 0
    # add every line to a list
    lines = f.readlines()

    # loop over every line
    for line in lines:
        firstNumber = ''
        lastNumber = ''
        lineSum = 0
        # loop over every character in the line
        for char in line:
            # check if character is a number and break the loop
            if char.isdigit():
                firstNumber = char
                break
        # loop backwards over every character in the line
        for char in reversed(line):
            # check if character is a number and break the loop
            if char.isdigit():
                lastNumber = char
                break
        lineSum = firstNumber + lastNumber
        sum += int(lineSum)

    # final result
    print(sum)

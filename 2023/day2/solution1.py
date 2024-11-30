# open and read the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    sum = 0

    # read each line
    for line in lines:
        possible_game = True
        # separate game infos and results
        games, results = line.split(":")

        # split number of game
        _, number_game = games.split()

        # separate results
        for result in results.split(";"):
            # separate each set of cubes
            for cubes in result.split(","):
                # separate color and count of each set
                count, color = cubes.split()
                if (color == "red" and int(count) > 12) or (color == "green" and int(count) > 13) or (color == "blue" and int(count) > 14):
                    possible_game = False
        if possible_game:
            sum += int(number_game)

    # final result
    print(sum)

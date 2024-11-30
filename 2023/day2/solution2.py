# open and read the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    power = 0

    # read each line
    for line in lines:
        possible_game = True
        # separate game infos and results
        games, results = line.split(":")

        number_of_red = 1
        number_of_green = 1
        number_of_blue = 1

        # split number of game
        _, number_game = games.split()

        # separate results
        for result in results.split(";"):
            # separate each set of cubes
            for cubes in result.split(","):
                # separate color and count of each set
                count, color = cubes.split()
                if color == "red" and int(count) > number_of_red:
                    number_of_red = int(count)
                if color == "green" and int(count) > number_of_green:
                    number_of_green = int(count)
                if color == "blue" and int(count) > number_of_blue:
                    number_of_blue = int(count)
        power += (number_of_red * number_of_green * number_of_blue)

    # final result
    print(power)

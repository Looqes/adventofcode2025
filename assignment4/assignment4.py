

# input_data = open("assignment4_testinput.txt").read().split("\n")
input_data = open("assignment4_input.txt").read().split("\n")

PART = 2

# preprocessing input....
input_data = [line for line in input_data]

def visualize_grid(grid):
    for row in grid:
        for character in row:
            print(character, end = "")
        print()



def count_adjacent_rolls(grid, x, y):
    rolls = 0
    grid_height = len(grid)
    grid_width = len(grid[0])
    # print(grid_height, grid_width)

    # print(f"Checking for {y, x}")

    for y_adj in range(max(y - 1, 0), min(y + 2, grid_height)):
        
        for x_adj in range(max(x - 1, 0), min(x + 2, grid_width)):
            if (y_adj, x_adj) == (y, x):
                # print("This is the middle spot, skip")
                continue
            # print(y_adj, x_adj, ": ", end = "")
            character_at_coordinates = grid[y_adj][x_adj]
            # print(character_at_coordinates)
            if character_at_coordinates == "@":
                rolls += 1

    return rolls


# Part 1
if PART == 1:
    accessible = 0
    # visualize_grid(input_data)

    for y, row in enumerate(input_data):
        for x, character in enumerate(row):
            # Check if a spot has a roll. If so, then check surrounding rolls.
            if input_data[y][x] == "@":
                rolls = count_adjacent_rolls(input_data, x, y)
                # print(f"Rolls: {rolls}. {"Accessible!!!!!" if rolls < 4 else "..."} \n")

                if rolls < 4:
                    accessible += 1

    print(f"Amount of accessible rolls: {accessible }")



input_data = [[character for character in row] for row in input_data]

# Part 2
if PART == 2:
    accessible = 0

    rolls_are_removable = True

    while rolls_are_removable:
        # visualize_grid(input_data)
        coordinates_of_accessible_rolls = set()

        for y, row in enumerate(input_data):
            for x, character in enumerate(row):
                # Check if a spot has a roll. If so, then check surrounding rolls.
                if input_data[y][x] == "@":
                    rolls = count_adjacent_rolls(input_data, x, y)

                    if rolls < 4:
                        accessible += 1

                        coordinates_of_accessible_rolls.add((y, x))

        if bool(coordinates_of_accessible_rolls):
            for y, x in coordinates_of_accessible_rolls:
                input_data[y][x] = "."
        else:
            rolls_are_removable = False

    print(f"Amount of accessible rolls: {accessible}")
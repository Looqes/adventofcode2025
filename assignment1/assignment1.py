

# puzzle 1
#######################
input_data = [item.strip() for item in open("assignment1_input.txt").readlines()]
input_data = [(item[0:1], int(item[1:])) for item in input_data]

dial = 50

amount_of_zeroes = 0

for direction, amount in input_data:
    if direction == "L":
        dial = dial - amount
        
        if dial < 0:
            dial = (100 + dial) % 100

    if direction == "R":
        dial = dial + amount

        if dial >= 100:
            dial = dial % 100

    if dial == 0:
        amount_of_zeroes += 1

print(amount_of_zeroes)



# puzzle 2
#######################

dial = 50

amount_of_zero_clicks = 0

for direction, amount in input_data:
    if direction == "L":
        for _ in range(amount):
            dial -= 1

            if dial == 0:
                amount_of_zero_clicks += 1
            if dial == -1:
                dial = 99
            

    elif direction == "R":
        for _ in range(amount):
            dial += 1

            if dial == 100:
                dial = 0
                amount_of_zero_clicks += 1
    



print(amount_of_zero_clicks)


import math

# input_data = open("assignment6_testinput.txt").read().split("\n")
input_data = open("assignment6_input.txt").read().split("\n")



PART = 2


if PART == 1:
    total_sum = 0

    input_data_processed = []
    for line in input_data:
        input_data_processed.append(line.strip().split())

    for i in range(len(input_data_processed)):
        if i < len(input_data) - 1:
            input_data_processed[i] = list(map(int, input_data_processed[i]))

    for i in range(len(input_data_processed[0])):
        operator = input_data_processed[-1][i]

        result = input_data_processed[0][i]
        print(f"{result}", end="")
        for row in input_data_processed[1:-1]:
            if operator == "+":
                print(f" + {row[i]}", end="")
                result += row[i]
            elif operator == "*":
                print(f" * {row[i]}", end="")
                result *= row[i]
        
        print(f" = {result}")

        total_sum += result

    print(f"\n###\nFinal result: {total_sum}")



if PART == 2:
    total_sum = 0
    operator = None
    equation_numbers = []

    for i in range(len(input_data[0])):
        # One iteration represents 1 column with 1 number
        column = []

        # update the operator when a new one is found in the bottom row
        if input_data[-1][i] != " ":
            operator = input_data[-1][i]

        # Iterate data column by column and apply the operator to the number formed by a column
        for row in input_data[:-1]:
            column.append(row[i])

        # Check if an empty column is reached, this marks the end of current equation
        if all([digit == " " for digit in column]):
            if operator == "*":
                equation_result = math.prod(equation_numbers)
            elif operator == "+":
                equation_result = sum(equation_numbers)
            print(f"result of current equation = {equation_result}")

            total_sum += equation_result
            equation_numbers = []

        else:
            column_number = int("".join(column).strip())
            equation_numbers.append(column_number)
            print(f"Column: {column}, giving number: {column_number}")
    
    # handle last column
    if operator == "*":
        equation_result = math.prod(equation_numbers)
    elif operator == "+":
        equation_result = sum(equation_numbers)
    print(f"result of current equation = {equation_result}")

    total_sum += equation_result
    equation_numbers = []

    print(f"\n########\nFinal result: {total_sum}")
    
        


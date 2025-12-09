

# input_data = open("assignment3_testinput.txt").read().split("\n")
input_data = open("assignment3_input.txt").read().split("\n")
 
PART = 2

# PART 1
if PART == 1:
    sum_of_max_jolts = 0

    for bank in input_data:
        print(f"bank: {bank}")
        bank = [battery for battery in bank]

        bank_max_jolt = 0

        for i, first_batt in enumerate(bank):
            for second_batt in bank[i + 1:]:
                jolt = int(first_batt + second_batt)
                
                if jolt > bank_max_jolt:
                    bank_max_jolt = jolt

        print(f"Bank max jolt = {bank_max_jolt}")
        sum_of_max_jolts += bank_max_jolt

    print(f"result = {sum_of_max_jolts}")
    


# PART 2
# Start by turning on all batteries, and then sequentially turn off low volt batteries
if PART == 2:
    sum_of_max_jolts = 0

    for bank in input_data:
        # print(f"bank: {bank}")
        bank_max_jolt = 0
        bank = [battery for battery in bank]
        biggest_batteries = []

        for i in range(1, 13):
            valid_range_to_check = bank[:-(12 - i)] if i < 12 else bank
            # print(f"Check max of {valid_range_to_check}")
            biggest_battery = max(valid_range_to_check)
            index_of_biggest_battery = bank.index(biggest_battery)
            # print(f"Biggest = {biggest_battery}, on position {index_of_biggest_battery}")

            biggest_batteries.append(
                biggest_battery
            )
            
            # print(f"Bank: {bank}, index of the biggest battery = {index_of_biggest_battery}")
            # print(f"{bank[index_of_biggest_battery + 1:]}")

            bank = bank[index_of_biggest_battery + 1:]
            # print(f"Continue checking with {"".join(bank)}")
            # print()

        # print(f"Biggest bank config: {biggest_batteries}")
        # print("---\n")
        
        bank_max_jolt = int("".join(biggest_batteries))

        # print(f"Bank max jolt = {bank_max_jolt}")
        sum_of_max_jolts += bank_max_jolt

    print(f"result = {sum_of_max_jolts}")
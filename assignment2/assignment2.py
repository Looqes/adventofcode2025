

PART = 2

# data = open("assignment2_testinput.txt").read().split(",")
data = open("assignment2_input.txt").read().split(",")
data_preprocessed = []


for pair in data:
    start_range, end_range = pair.split("-")
    start_range = int(start_range)
    end_range = int(end_range)

    data_preprocessed.append((start_range, end_range))



def even_number_of_digits(number):
    return len(str(number)) % 2 == 0

def check_uneven_clause(start_range, end_range):
    return (
        len(str(start_range)) == len(str(end_range)) and
        not even_number_of_digits(start_range) and
        not even_number_of_digits(end_range)
    )

def check_symmetric_number(number):
    id = str(number)
    if (
        len(id) % 2 == 0 and
        id[:int((len(id)/2))] == id[int((len(id)/2)):]
    ):
        return number
    else:
        return None


sum_of_ids = 0

if PART == 1:
    for start_range, end_range in data_preprocessed:
        if check_uneven_clause(start_range, end_range):
            print("Uneven number of digits for both numbers, range cant contain repeating sequences")
        else:
            for id in range(start_range, end_range + 1):
                result = check_symmetric_number(id)

                if result:
                    print(f"Found silly pattern: {result}")
                    sum_of_ids += result

    print(f"Final result sum of bad ids: {sum_of_ids}")


if PART == 2:
    sum_of_ids = 0

    for idrange in data_preprocessed:
        for id in range(idrange[0], idrange[1] + 1):
            id = str(id)

            for i in range(len(id) // 2):
                div, rem = divmod(len(id), i + 1)

                if rem == 0 and id[0 : i + 1] * div == id:
                    sum_of_ids += int(id) 
                    break
    print(f"Final result sum of bad ids: {sum_of_ids}")

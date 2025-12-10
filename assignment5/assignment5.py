
PART = 2

input_data = [
    part.split("\n") 
    for part in
    # open("assignment5_testinput.txt").read().split("\n\n")
    open("assignment5_input.txt").read().split("\n\n")
]

ranges, ingredients = input_data

# print(f"{ranges}")
# print(f"{ingredients}")


if PART == 1: 
    ranges = [
        (start, end)
        for id_range in ranges
        for start, end in [tuple(map(int, id_range.split("-")))]
    ]

    ingredients = list(map(int, ingredients))

    fresh_ingredients = 0
    for ingredient in ingredients:
        for start, end in ranges:
            if ingredient >= start and \
                ingredient <= end:
                # ingredient is fresh
                fresh_ingredients += 1
                break

    print(fresh_ingredients)




if PART == 2:
    ranges = [
        (start, end)
        for id_range in ranges
        for start, end in [tuple(map(int, id_range.split("-")))]
    ]

    amount_of_fresh_ids = 0

    for i, id_range in enumerate(ranges):
        start, end = id_range
        # print(start, end)

        for j, other_id_range in enumerate(ranges[i + 1:]):
            o_start, o_end = other_id_range
            # print(f"  {o_start, o_end}")

            # check if overlap
            # left overlap
            if o_start <= start and \
                start <= o_end:
                # print("Left overlap")
                start = o_end + 1
                # print(f"  Range is now {start, end}")
                
                if start > end:
                    start, end = None, None
                    break

            # right overlap
            if o_start <= end and \
                end <= o_end:
                # print("Right overlap")
                end = o_start - 1
                # print(f"  Range is now {start, end}")

                if start > end:
                    start, end = None, None
                    break
        # print()

        if (start, end) != (None, None):
            amount_of_fresh_ids += (end - start) + 1

    
    print(amount_of_fresh_ids)

